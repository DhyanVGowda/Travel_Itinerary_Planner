import re
import time
from datetime import datetime

import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

from rest_api import *


def is_valid_us_mobile_number(number):
    # Regular expression for a 10-digit US mobile number in various formats
    pattern = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
    return bool(re.match(pattern, number))


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def signup_page():
    with st.form("signup_form"):
        st.subheader('Sign Up')
        email = st.text_input('Email')
        mobile = st.text_input('Mobile')
        fname = st.text_input('First Name')
        lname = st.text_input('Last Name')
        gen = st.selectbox('Gender', ['Male', 'Female', 'Other', 'Prefer not to say'])
        dob = st.date_input('Date of Birth', None)
        unit = st.text_input('Unit')
        street = st.text_input('Street')
        street_no = st.text_input('Street Number')
        city = st.text_input('City')
        state = st.text_input('State')
        zip_code = st.text_input('Zip Code')
        signup_button = st.form_submit_button('Sign Up')

        if signup_button:
            if not email or not mobile or not fname:
                st.error('Email, mobile, and first name are compulsory')
            elif not is_valid_us_mobile_number(mobile):
                st.error('Please enter a valid Phone number')
            elif not is_valid_email(email):
                st.error('Please enter a valid email address')
            else:
                signup_data = {
                    'email': email,
                    'mobile': mobile,
                    'fname': fname,
                    'lname': lname,
                    'gen': gen,
                    'dob': dob.isoformat() if dob else None,  # converting date to string
                    'unit': unit,
                    'street': street,
                    'street_no': street_no,
                    'city': city,
                    'state': state,
                    'zip': zip_code
                }
                response = signup_user(signup_data)
                if response.status_code == 201:
                    st.success('Signup successful. You can log in to your account.')
                else:
                    st.error('Signup failed. Error: ' + response.json().get('error', ''))


def login_page():
    with st.form("login_form"):
        st.subheader('Login')
        login_email = st.text_input('Email', key='login_email')
        login_password = st.text_input('Password', type='password', key='login_password')
        login_button = st.form_submit_button('Login')

        if login_button:
            login_data = {
                'email': login_email,
                'password': login_password
            }
            response = login_user(login_data)
            if response.status_code == 200:
                st.session_state['user_email'] = login_email
                st.session_state['f_name'] = response.json()[2]
                st.rerun()  # This reruns the script to switch to the trips display
            else:
                st.error('Login failed. Incorrect email or password.')


def display_trips():
    st.subheader("Your Trips")

    # First, display existing trips if any
    if 'user_email' in st.session_state:
        trips_df, error = fetch_trips(st.session_state['user_email'])
        if not trips_df.empty:

            st.dataframe(trips_df, hide_index=True)

            with st.expander("Add Travellers"):

                with st.form("add_traveller_form", clear_on_submit=True):
                    st.subheader('Add Traveller to Trip')
                    trip_options_add = trips_df['Trip Id'].unique()
                    trip_options_add = [int(trip_id) for trip_id in trip_options_add]
                    selected_trip_id = st.selectbox('Select Trip ID', trip_options_add)
                    traveller_email = st.text_input('New Traveller Email')
                    submit_add_traveller = st.form_submit_button('Add Traveller')

                    if submit_add_traveller:
                        if not traveller_email:
                            st.error('Traveller email is required.')
                        else:
                            payload = {
                                "trip_id": selected_trip_id,
                                "email": traveller_email
                            }
                            response = add_traveller_to_trip(payload)
                            if response.status_code == 201:
                                st.success('Traveller added successfully to the trip.')
                                time.sleep(1)
                                st.experimental_rerun()
                            else:
                                st.error(f'Failed to add traveller to the trip. Error: {response.json()["error"]}')

            with st.expander("Delete Trip"):
                trip_options_add = trips_df['Trip Id'].unique()
                trip_options_add = [int(trip_id) for trip_id in trip_options_add]
                selected_trip_id = st.selectbox('Select Trip ID', trip_options_add)
                if st.button('Delete Trip'):
                    response = delete_trip(selected_trip_id)
                    if response.status_code == 200:
                        st.success(f"Trip deleted successfully.")
                        time.sleep(1)
                        st.experimental_rerun()
                    else:
                        st.error('Failed to delete the trip.')

            with st.expander("Update Trip"):
                selected_trip_id = st.selectbox('Select Trip ID to update', list(trips_df['Trip Id']))
                selected_trip = trips_df[trips_df['Trip Id'] == selected_trip_id].iloc[0]

                with st.form("update_trip_form", clear_on_submit=True):
                    st.subheader('Update Trip')
                    st.text_input('Trip ID', value=selected_trip['Trip Id'], key='trip_id', disabled=True)
                    trip_name = st.text_input('Trip Name', value=selected_trip['Trip Name'], key='trip_name')
                    if not pd.isna(selected_trip['Start Date']):
                        start_date = st.date_input('Start Date', value=pd.to_datetime(selected_trip['Start Date']),
                                                   key='start_date')
                    else:
                        start_date = st.date_input('Start Date', key='start_date')
                    if not pd.isna(selected_trip['End Date']):
                        end_date = st.date_input('End Date', value=pd.to_datetime(selected_trip['End Date']),
                                                 key='end_date')
                    else:
                        end_date = st.date_input('End Date', key='end_date')
                    status = st.selectbox('Status',
                                          ['Planning In Progress', 'Planned Successfully', 'Ongoing', 'Completed'],
                                          index=['Planning In Progress', 'Planned Successfully', 'Ongoing',
                                                 'Completed'].index(selected_trip['Trip Status']), key='trip_status')
                    submit_update_trip = st.form_submit_button('Update Trip')

                    if submit_update_trip:
                        update_trip_data = {
                            'trip_name': trip_name,
                            'start_date': start_date.isoformat() if start_date else None,
                            'end_date': end_date.isoformat() if end_date else None,
                            'trip_status': status
                        }
                        response = update_trip(selected_trip_id, update_trip_data)
                        if response:
                            st.success(f"Trip with ID {selected_trip_id} updated successfully.")
                            time.sleep(1)
                            st.experimental_rerun()
                        else:
                            st.error(f"Failed to update trip with ID {selected_trip_id}.")

        else:
            st.error(error or "No trips found.")

    # Interface to add a new trip
    st.subheader('Add New Trip')
    with st.form("add_trip_form", clear_on_submit=True):
        new_trip_name = st.text_input('Trip Name')
        new_start_date = st.date_input('Start Date', None)
        new_end_date = st.date_input('End Date', None)
        new_status = st.selectbox('Status', ['Planning In Progress', 'Planned Successfully', 'Ongoing', 'Completed'])
        submit_new_trip = st.form_submit_button('Add Trip')

        if submit_new_trip:
            if not new_trip_name:
                st.error('Trip Name is required.')
            else:
                new_trip_data = {
                    'email': st.session_state['user_email'],
                    'trip_name': new_trip_name,
                    'start_date': new_start_date.isoformat() if new_start_date else None,
                    'end_date': new_end_date.isoformat() if new_end_date else None,
                    'trip_status': new_status
                }
                response = add_trip(new_trip_data)  # Make sure this function is implemented to send the POST request
                if response.status_code == 201:
                    st.success('New trip added successfully.')
                    time.sleep(1)
                    st.experimental_rerun()

                else:
                    st.error('Failed to add new trip.')


def login_page():
    with st.form("login_form"):
        st.subheader('Login')
        login_email = st.text_input('Email', key='login_email')
        login_password = st.text_input('Password', type='password', key='login_password')
        login_button = st.form_submit_button('Login')

        if login_button:
            login_data = {
                'email': login_email,
                'password': login_password
            }
            response = login_user(login_data)
            if response.status_code == 200:
                user_info = response.json()  # Assuming the response contains user info
                st.session_state['user_email'] = login_email
                st.session_state['user_info'] = user_info  # Store user info in session state
                st.session_state['traveller_details'] = user_info
                st.experimental_rerun()
            else:
                st.error('Login failed. Incorrect email or password.')


def show_user_info():
    # Get the logged-in user's email from the session state
    email = st.session_state.get('user_email', '')

    # If there is an email in the session state, attempt to fetch user info
    if email:
        # Fetch the user information, which should be a list
        user_info = st.session_state.get('traveller_details', [])

        # Check if the response is not empty
        if user_info:
            # Assuming the order of user_info list is consistent with the API response
            st.sidebar.header('**Traveler Information**')
            st.sidebar.markdown(f"**Name:** {user_info[2]} {user_info[3]}")  # Name in bold
            st.sidebar.markdown(f"**Email:** {user_info[0]}")  # Index for email
            st.sidebar.write(f"**Mobile:** {user_info[1]}")  # Index for mobile
            st.sidebar.write(f"**Unit No.:** {user_info[6]}")  # Index for unit and street
            st.sidebar.write(f"**Street Name:** {user_info[7]}")  # Index for unit and street
            st.sidebar.write(f"**Street Number:** {user_info[8]}")  # Index for unit and street
            st.sidebar.write(f"**City:** {user_info[9]}")  # Index for city
            st.sidebar.write(f"**State:** {user_info[10]}")  # Index for state
            st.sidebar.write(f"**Zipcode:** {user_info[11]}")  # Index for state
        else:
            # If there is no user info or an empty response, display an error message
            st.sidebar.error("Failed to load traveler information.")
    else:
        # If there is no email in the session state, prompt the user to log in
        st.sidebar.write("Please log in to see traveler information.")


def edit_user_info(user_info):
    with st.sidebar:
        with st.expander('Update Traveller Info'):
            st.subheader("Update User Info")
            # Create input fields for editable fields
            new_first_name = st.text_input("First Name", value=user_info[2])
            new_last_name = st.text_input("Last Name", value=user_info[3])
            new_unit = st.text_input("New Unit No.", value=user_info[6])
            new_street_name = st.text_input("New Street Name", value=user_info[7])
            new_street_number = st.text_input("New Street No.", value=user_info[8])
            new_city = st.text_input("New City", value=user_info[9])
            new_state = st.text_input("New State", value=user_info[10])
            new_zip = st.text_input("New zipcode", value=user_info[11])

            # Button to submit changes
            if st.button("Submit Changes"):
                # Construct updated user info

                updated_user_info = user_info.copy()
                updated_user_info[2] = new_first_name
                updated_user_info[3] = new_last_name
                updated_user_info[6] = new_unit
                updated_user_info[7] = new_street_name
                updated_user_info[8] = new_street_number
                updated_user_info[9] = new_city
                updated_user_info[10] = new_state
                updated_user_info[11] = new_zip

                # Call update_user_info function
                user_email = st.session_state['user_email']
                user_update_request = construct_user_update_request(updated_user_info, user_email)

                response = update_user_info(user_update_request, st.session_state['user_email'])
                if response:
                    st.success("User information updated successfully.")
                else:
                    st.error("Failed to update user information.")


def construct_user_update_request(updated_user_info, user_email):
    user_update_request = {
        "first_name": updated_user_info[2],
        "last_name": updated_user_info[3],
        "gender": updated_user_info[4],  # Assuming gender is at index 4 in user_info
        "unit_number": updated_user_info[6],  # Assuming unit number is at index 7 in user_info
        "street_name": updated_user_info[7],  # Assuming street name is at index 8 in user_info
        "street_number": updated_user_info[8],  # Assuming street number is at index 6 in user_info
        "city": updated_user_info[9],  # Assuming city is at index 9 in user_info
        "state": updated_user_info[10],  # Assuming state is at index 10 in user_info
        "zipcode": updated_user_info[11],  # Assuming zipcode is at index 11 in user_info
        "email": user_email
    }
    return user_update_request


def add_hotel_page(trip_ids):
    destinations_df, error = get_destinations(trip_ids)
    if not destinations_df.empty:
        with st.form("add_hotel_form", clear_on_submit=True):
            st.subheader("Add Hotel Accommodation")
            destination_options = list(destinations_df['destination_id'])
            selected_destination_id = st.selectbox('Select Destination ID', destination_options)
            accommodation_name = st.text_input('Accommodation Name')
            cost_per_night = st.number_input('Cost Per Night', step=100)
            telephone_number = st.text_input('Telephone Number')
            checkin_date = st.date_input('Check-in Date', None)
            checkout_date = st.date_input('Check-out Date', None)
            street_name = st.text_input('Street Name')
            street_number = st.text_input('Street Number')
            city = st.text_input('City')
            state = st.text_input('State')
            zipcode = st.text_input('Zip Code')
            number_of_rooms = st.number_input('Number of Rooms', min_value=1, value=1)
            meal_included = st.checkbox('Meal Included?')
            star_rating = st.selectbox('Star Rating', ['1', '2', '3', '4', '5'])
            submit_button = st.form_submit_button('Add Hotel')

            if submit_button:
                if not accommodation_name or not cost_per_night or not telephone_number:
                    st.error('Accommodation name, cost per night, and telephone number are required.')
                else:
                    hotel_data = {
                        "accommodation_name": accommodation_name,
                        "cost_per_night": cost_per_night,
                        "telephone_number": telephone_number,
                        "checkin_date": checkin_date.isoformat() if checkin_date else None,
                        "checkout_date": checkout_date.isoformat() if checkout_date else None,
                        "street_name": street_name,
                        "street_number": street_number,
                        "city": city,
                        "state": state,
                        "zipcode": zipcode,
                        "destination_id": selected_destination_id,
                        "number_of_rooms": number_of_rooms,
                        "meal": meal_included,
                        "star_rating": star_rating
                    }
                    response = add_hotel(hotel_data)
                    if response.status_code == 201:
                        st.success('Hotel added successfully.')
                        time.sleep(1)
                        st.experimental_rerun()
                    else:
                        st.error('Failed to add hotel.')
    else:
        st.error('Add destinations.')


def add_homestay_page(trip_ids):
    destinations_df, error = get_destinations(trip_ids)
    if not destinations_df.empty:
        with st.form("add_homestay_form", clear_on_submit=True):
            st.subheader("Add Homestay Accommodation")
            destination_options = list(destinations_df['destination_id'])
            selected_destination_id = st.selectbox('Select Destination ID', destination_options)
            accommodation_name = st.text_input('Accommodation Name')
            cost_per_night = st.number_input('Cost Per Night (dollars)', step=100)
            telephone_number = st.text_input('Telephone Number')
            checkin_date = st.date_input('Check-in Date', None)
            checkout_date = st.date_input('Check-out Date', None)
            street_name = st.text_input('Street Name')
            street_number = st.text_input('Street Number')
            city = st.text_input('City')
            state = st.text_input('State')
            zipcode = st.text_input('Zip Code')
            number_of_rooms = st.number_input('Number of Rooms', min_value=1, value=1)
            is_cook_available = st.checkbox('Is Cook Available?')
            stay_type = st.selectbox('Stay Type', ['Private', 'Shared'])
            is_pet_allowed = st.checkbox('Is Pet Allowed?')
            submit_button = st.form_submit_button('Add Homestay')

            if submit_button:
                if not accommodation_name or not cost_per_night or not telephone_number:
                    st.error('Accommodation name, cost per night, and telephone number are required.')
                else:
                    homestay_data = {
                        "accommodation_name": accommodation_name,
                        "cost_per_night": cost_per_night,
                        "telephone_number": telephone_number,
                        "checkin_date": checkin_date.isoformat() if checkin_date else None,
                        "checkout_date": checkout_date.isoformat() if checkout_date else None,
                        "street_name": street_name,
                        "street_number": street_number,
                        "city": city,
                        "state": state,
                        "zipcode": zipcode,
                        "destination_id": selected_destination_id,
                        "number_of_rooms": number_of_rooms,
                        "is_cook_available": is_cook_available,
                        "stay_type": stay_type,
                        "is_pet_allowed": is_pet_allowed
                    }
                    response = add_homestay(homestay_data)
                    if response.status_code == 201:
                        st.success('Homestay added successfully.')
                        time.sleep(1)
                        st.experimental_rerun()
                    else:
                        st.error('Failed to add homestay.')
    else:
        st.error('Add destinations.')


def add_hostel_page(trip_ids):
    destinations_df, error = get_destinations(trip_ids)
    if not destinations_df.empty:
        with st.form("add_hostel_form", clear_on_submit=True):
            st.subheader("Add Hostel Accommodation")
            destination_options = list(destinations_df['destination_id'])
            selected_destination_id = st.selectbox('Select Destination ID', destination_options)
            accommodation_name = st.text_input('Accommodation Name')
            cost_per_night = st.number_input('Cost Per Night', step=100)
            telephone_number = st.text_input('Telephone Number')
            checkin_date = st.date_input('Check-in Date', None)
            checkout_date = st.date_input('Check-out Date', None)
            street_name = st.text_input('Street Name')
            street_number = st.text_input('Street Number')
            city = st.text_input('City')
            state = st.text_input('State')
            zipcode = st.text_input('Zip Code')
            number_of_rooms = st.number_input('Number of Rooms', min_value=1, value=1)
            meal_included = st.checkbox('Meal Included?')
            bath_type = st.selectbox('Bath Type', ['Private', 'Shared'])
            wifi_available = st.checkbox('WiFi Available?')
            mixed_dorm = st.checkbox('Mixed Dorm?')
            submit_button = st.form_submit_button('Add Hostel')

            if submit_button:
                if not accommodation_name or not cost_per_night or not telephone_number:
                    st.error('Accommodation name, cost per night, and telephone number are required.')
                else:
                    hostel_data = {
                        "accommodation_name": accommodation_name,
                        "cost_per_night": cost_per_night,
                        "telephone_number": telephone_number,
                        "checkin_date": checkin_date.isoformat() if checkin_date else None,
                        "checkout_date": checkout_date.isoformat() if checkout_date else None,
                        "street_name": street_name,
                        "street_number": street_number,
                        "city": city,
                        "state": state,
                        "zipcode": zipcode,
                        "destination_id": selected_destination_id,
                        "number_of_rooms": number_of_rooms,
                        "meal": meal_included,
                        "bath_type": bath_type,
                        "wifi": wifi_available,
                        "mixed_dorm": mixed_dorm
                    }
                    response = add_hostel(hostel_data)
                    if response.status_code == 201:
                        st.success('Hostel added successfully.')
                        time.sleep(1)
                        st.experimental_rerun()
                    else:
                        st.error('Failed to add hostel.')
    else:
        st.error('Add destinations.')


def display_destinations():
    st.subheader("Destinations")

    if 'user_email' in st.session_state:
        trips_df, error = fetch_trips(st.session_state['user_email'])
        if not trips_df.empty:
            trip_ids = trips_df['Trip Id'].tolist()
            destinations_df, error = get_destinations(trip_ids)
            if not destinations_df.empty:
                selected_columns_df = destinations_df[['trip_id', 'destination_id', 'destination_name']]

                remaining_columns_df = destinations_df.drop(columns=['trip_id', 'destination_id', 'destination_name'])

                modified_destinations_df = pd.concat([selected_columns_df, remaining_columns_df], axis=1)
                st.dataframe(modified_destinations_df)

                with st.expander("Delete Destinations"):
                    trip_options = list(destinations_df['trip_id'])
                    selected_trip_id_delete = st.selectbox('Select Trip Id to delete', trip_options)
                    destinations_options = list(destinations_df['destination_id'])
                    selected_destn_id_delete = st.selectbox('Select Destination Id to delete', destinations_options)
                    if st.button('Delete Destination'):
                        response = delete_destination(selected_trip_id_delete, selected_destn_id_delete)
                        if response.status_code == 200:
                            st.success(f"Destination deleted successfully.")
                            time.sleep(1)
                            st.experimental_rerun()
                        else:
                            st.error('Failed to delete the Destination.' + response.json().get('error'))

                # "Update Destination" section moved outside of the "Delete Destinations" expander
                with st.expander("Update Destination"):
                    trip_options_update = list(destinations_df['trip_id'])
                    selected_trip_id_update = st.selectbox('Select Trip Id to update', trip_options_update)
                    destinations_options_update = list(destinations_df['destination_id'])
                    selected_destn_id_update = st.selectbox('Select Destination Id to update',
                                                            destinations_options_update)
                    selected_destination = destinations_df[(destinations_df['trip_id'] == selected_trip_id_update) & (
                            destinations_df['destination_id'] == selected_destn_id_update)].iloc[0]
                    edit_destination_info(selected_destination)

            with st.form("add_destination_form", clear_on_submit=True):
                st.subheader("Add Destination to Trip")
                trip_options_add = trips_df['Trip Id'].unique()
                trip_options_add = [int(trip_id) for trip_id in trip_options_add]
                selected_trip_id_add = st.selectbox('Select Trip ID', trip_options_add)
                destination_name = st.text_input('Destination Name')
                country = st.text_input('Country')
                arrival_date = st.date_input('Arrival Date', None)
                departure_date = st.date_input('Departure Date', None)
                transport_mode = st.text_input('Transport Mode')
                travel_duration = st.text_input('Travel Duration (in HH:mm format)')
                submit_button = st.form_submit_button('Add Destination')
                if submit_button:
                    if not destination_name or not country:
                        st.error('Destination name and country are required.')
                    else:
                        destination_data = {
                            "trip_id": selected_trip_id_add,
                            "destination_name": destination_name,
                            "country": country,
                            "arrival_date": arrival_date.isoformat() if arrival_date else None,
                            "departure_date": departure_date.isoformat() if departure_date else None,
                            "transport_mode": transport_mode,
                            "travel_duration": travel_duration
                        }
                        response = add_destination_to_trip(destination_data)
                        if response.status_code == 201:
                            st.success('Destination added to trip successfully.')
                            time.sleep(1)
                            st.experimental_rerun()
                        else:
                            st.error('Failed to add destination to trip.')
        else:
            st.error("No trips found to display destinations.")
    else:
        st.error("Please log in to view destinations.")


def edit_destination_info(destination_info):
    st.subheader("Update Destination Info")
    # Create input fields for editable fields
    new_destination_name = st.text_input("New Destination Name", value=destination_info['destination_name'])
    new_country = st.text_input("New Country", value=destination_info['country'])
    new_arrival_date = st.date_input("New Arrival Date", value=pd.to_datetime(destination_info['arrival_date']),
                                     key='new_arrival_date')
    new_departure_date = st.date_input("New Departure Date", value=pd.to_datetime(destination_info['departure_date']),
                                       key='new_departure_date')
    new_transport_mode = st.text_input("New Transport Mode", value=destination_info['transportation_mode'])

    # for column_name, column_data in destination_info.items():
    #     try:
    #         # Attempt to access the first element
    #         first_element = column_data.iloc[0]
    #         print(f"Column '{column_name}' has data type: {type(first_element)}")
    #     except AttributeError:
    #         # Skip columns with non-iterable data types
    #         print(f"Column '{column_name}' contains non-iterable data type: {type(column_data)}")

    if destination_info['travel_duration'] is None or destination_info['travel_duration'] == '':
        new_travel_duration = st.time_input("New Travel Duration", None)
    else:
        # Convert string to time object if not None or empty
        new_travel_duration = datetime.strptime(destination_info['travel_duration'], '%H:%M:%S').time()
        # Provide the time object as the default value
        new_travel_duration = st.time_input("New Travel Duration", value=new_travel_duration)

    # Button to submit changes
    if st.button("Submit Update for Destination"):
        # Construct updated destination info
        updated_destination_info = {
            'destination_id': str(destination_info['destination_id']),
            'trip_id': str(destination_info['trip_id']),
            'destination_name': new_destination_name,
            'country': new_country,
            'arrival_date': new_arrival_date.isoformat() if new_arrival_date else None,
            'departure_date': new_departure_date.isoformat() if new_departure_date else None,
            'transport_mode': new_transport_mode,
            'travel_duration': new_travel_duration.strftime('%H:%M:%S') if new_travel_duration else None,
        }

        # Call update_destination_info function
        response = update_destination_info(updated_destination_info)
        if response:
            st.success("Destination information updated successfully.")
            time.sleep(1);
            st.experimental_rerun()
        else:
            st.error("Failed to update destination information.")


def display_activities():
    st.subheader("User's Activity Data")
    if 'user_email' in st.session_state:
        trips_df, error = fetch_trips(st.session_state['user_email'])
        if not trips_df.empty:
            trip_ids = trips_df['Trip Id'].tolist()  # Assuming 'Trip Id' is the correct column name
            activity_df, error = get_activities(trip_ids)
            if not activity_df.empty:
                st.dataframe(activity_df)

                with st.expander("Delete Activity"):
                    activity_options = list(activity_df['activity_id'])
                    selected_activity_id = st.selectbox('Select Activity ID', activity_options)
                    if st.button('Delete Activity'):
                        response = delete_activity(selected_activity_id)
                        if response.status_code == 200:
                            st.success("Activity deleted successfully.")
                            time.sleep(1)
                            st.experimental_rerun()
                        else:
                            st.error(f"Failed to delete activity. Error: {response.json().get('error')}")
            else:
                st.error(error or "No Activity found.")

            add_activity_page(trip_ids)
        else:
            st.error("No activity found to display.")
    else:
        st.error("Please log in to view Activities Data.")


def display_accommodations():
    st.subheader("User's Accomodations")
    options = ["Hotel", "Hostel", "Homestay"]
    selected = option_menu("Sort by Accomodation Type", options,
                           orientation="horizontal")
    if selected == "Homestay":
        if 'user_email' in st.session_state:
            trips_df, error = fetch_trips(st.session_state['user_email'])
            if not trips_df.empty:
                trip_ids = trips_df['Trip Id'].tolist()  # Assuming 'Trip Id' is the correct column name
                homestay_df, error = get_accomodation_homestays(trip_ids)
                if not homestay_df.empty:
                    st.dataframe(homestay_df)
                    with st.expander("Delete Homestay"):
                        homstay_options = list(homestay_df['accommodation_id'])
                        selected_homestay_id = st.selectbox('Select Homestay ID', homstay_options)
                        if st.button('Delete Homestay'):
                            response = delete_homestay(selected_homestay_id)
                            if response.status_code == 200:
                                st.success(f"Homestay deleted successfully.")
                                time.sleep(1)
                                st.experimental_rerun()
                            else:
                                st.error('Failed to delete the Homestay.')
                else:
                    st.error(error or "No homestay Accomodation found.")

                add_homestay_page(trip_ids)
            else:
                st.error("No trips found to display.")
        else:
            st.error("Please log in to view accomodations.")

    if selected == "Hostel":
        if 'user_email' in st.session_state:
            trips_df, error = fetch_trips(st.session_state['user_email'])
            if not trips_df.empty:
                trip_ids = trips_df['Trip Id'].tolist()  # Assuming 'Trip Id' is the correct column name
                hostel_df, error = get_accomodation_hostels(trip_ids)
                if not hostel_df.empty:
                    st.dataframe(hostel_df)
                    with st.expander("Delete Hostel"):
                        hostel_options = list(hostel_df['accommodation_id'])
                        selected_hostel_id = st.selectbox('Select Hostel ID', hostel_options)
                        if st.button('Delete Hostel'):
                            response = delete_hostel(selected_hostel_id)
                            if response.status_code == 200:
                                st.success(f"Hostel deleted successfully.")
                                time.sleep(1)
                                st.experimental_rerun()
                            else:
                                st.error('Failed to delete the Hostel.')
                else:
                    st.error(error or "No Hostel Accomodation found.")
                add_hostel_page(trip_ids)
            else:
                st.error("No trips found to display.")
        else:
            st.error("Please log in to view accomodations.")

    if selected == "Hotel":
        if 'user_email' in st.session_state:
            trips_df, error = fetch_trips(st.session_state['user_email'])
            if not trips_df.empty:
                trip_ids = trips_df['Trip Id'].tolist()  # Assuming 'Trip Id' is the correct column name
                hotel_df, error = get_accomodation_hotels(trip_ids)
                if not hotel_df.empty:
                    st.dataframe(hotel_df)

                    with st.expander("Delete Hotel"):
                        hotel_options = list(hotel_df['accommodation_id'])
                        selected_hotel_id = st.selectbox('Select Hotel ID', hotel_options)
                        if st.button('Delete Hotel'):
                            response = delete_hotel(selected_hotel_id)
                            if response.status_code == 200:
                                st.success(f"Hotel deleted successfully.")
                                time.sleep(1)
                                st.experimental_rerun()
                            else:
                                st.error('Failed to delete the Hotel.')

                else:
                    st.error(error or "No Hotel Accomodation found.")

                add_hotel_page(trip_ids)
            else:
                st.error("No trips found to display.")
        else:
            st.error("Please log in to view accomodations.")


def display_expenses():
    st.subheader("Expenses")
    if 'user_email' in st.session_state:
        trips_df, error = fetch_trips(st.session_state['user_email'])
        if not trips_df.empty:
            trip_options_add = trips_df['Trip Id'].unique()
            trip_options_add = [int(trip_id) for trip_id in trip_options_add]
            selected_trip_id = st.selectbox('Select a Trip ID to manage expenses', trip_options_add)

            expenses, error = fetch_expenses(selected_trip_id)
            if expenses:
                expenses_df = pd.DataFrame(expenses)
                st.dataframe(expenses_df)

                with st.expander("Delete Expense"):
                    expense_ids = expenses_df['expense_id'].tolist()
                    selected_expense_id = st.selectbox("Select an Expense ID to delete", expense_ids)
                    if st.button('Delete Expense'):
                        response = delete_expense(selected_expense_id)
                        if response.status_code == 200:
                            st.success("Expense deleted successfully.")
                            time.sleep(1)
                            st.experimental_rerun()
                        else:
                            st.error(f"Failed to delete expense. Error: {response.json().get('error')}")
            else:
                st.error(error or "No expenses found for the selected trip.")

            with st.expander("Add Expense"):
                with st.form("add_expense_form", clear_on_submit=True):
                    expense_date = st.date_input("Date")
                    expense_category = st.text_input("Category")
                    expense_description = st.text_area("Description")
                    amount = st.number_input("Amount", min_value=0.0, format='%f')
                    currency = st.text_input("Currency", value="USD")
                    submit_button = st.form_submit_button("Add Expense")

                    if submit_button:
                        expense_data = {
                            "expense_date": expense_date.isoformat(),
                            "expense_category": expense_category,
                            "expense_description": expense_description,
                            "amount": amount,
                            "currency": currency,
                            "trip_id": selected_trip_id
                        }
                        response = create_expense(expense_data)
                        if response.status_code == 201:
                            st.success("Expense added successfully.")
                            time.sleep(1)
                            st.experimental_rerun()
                        else:
                            st.error(f"Failed to add expense. Error: {response.json().get('error')}")

    else:
        st.error("Please log in to view and manage expenses.")


def main():
    st.title('Travel Itinerary')

    # Sidebar menu
    options = ["Home", "Sign Up", "Login"]
    icons = ["house", "person-plus", "door-open"]

    # If user is logged in, show their info in the sidebar
    if 'user_email' in st.session_state:
        st.sidebar.image('../../resource/tgroup_travllers.jpg', caption='To Infinity and Beyond!')
        show_user_info()
        edit_user_info(st.session_state.get('traveller_details', []))
        options.remove("Sign Up")
        options.remove("Login")
        icons.remove("person-plus")
        icons.remove("door-open")
        options = ["Home", "Planned Trips", "Destinations", "Activities", "Accommodations", "Expenses",
                   "Essential Items", "All Trips", "Logout"]
        icons = ["house", "map", "globe", "building", "compass", "credit-card", "list", "clipboard-data",
                 "box-arrow-right"]

    selected = option_menu("Main Menu", options, icons=icons, menu_icon="cast", default_index=0,
                           orientation="horizontal")

    if selected == "Home":
        st.subheader("Welcome to the Travel Itinerary App!")
        st.subheader("Streamline Your Travels: Plan, Explore, Thrive!")
        if 'user_email' in st.session_state:
            st.write("Logged in as:", st.session_state['user_email'])

        st.image('../../resource/group_of_travellers.png', caption='Accio Memories: Magical Travel Awaits')
    elif selected == "Sign Up":
        signup_page()
    elif selected == "Login":
        login_page()
    elif selected == "Planned Trips" and 'user_email' in st.session_state:
        display_trips()
    elif selected == "Destinations" and 'user_email' in st.session_state:
        display_destinations()
    elif selected == "Activities" and 'user_email' in st.session_state:
        display_activities()
    elif selected == "Accommodations" and 'user_email' in st.session_state:
        display_accommodations()
    elif selected == "Expenses" and 'user_email' in st.session_state:
        display_expenses()
    elif selected == "Essential Items" and 'user_email' in st.session_state:
        display_essential_items()
    elif selected == "All Trips":
        display_all_trips_with_procedures()
        display_all_trips_without_procedures()
    elif selected == "Logout":
        for key in ['user_email', 'user_info']:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()


def add_activity_page(trip_ids):
    destination_df, error = get_destinations(trip_ids)
    if not destination_df.empty:
        st.subheader("Add Activity")
        activity_type = st.selectbox("Select Type of Activity", ["Sightseeing", "Adventure Sport", "Other"])

        if activity_type == "Sightseeing":
            add_sightseeing_activity_form(destination_df['destination_id'])
        elif activity_type == "Adventure Sport":
            add_adventure_sport_activity_form(destination_df['destination_id'])
        elif activity_type == "Other":
            add_other_activity_form(destination_df['destination_id'])


def add_sightseeing_activity_form(destination_options):
    with st.form("add_sightseeing_activity_form", clear_on_submit=True):
        st.subheader("Add Sightseeing Activity")

        destination_id = st.selectbox('Select Destination ID', destination_options)
        activity_location = st.text_input('Activity Location')
        activity_description = st.text_area('Activity Description')
        activity_date = st.date_input('Activity Date', None)
        start_time = st.time_input('Start Time', None)
        end_time = st.time_input('End Time', None)
        cost = st.number_input('Cost', step=10)
        site_type = st.text_input('Site Type')
        site_description = st.text_area('Site Description')

        submit_button = st.form_submit_button('Add Sightseeing Activity')

        if submit_button:
            if not site_type or not site_description:
                st.error("Site Type and Site Descriptions can't be empty for adding Sightseeing Activity.")
            else:
                sightseeing_data = {
                    "activity_location": activity_location,
                    "activity_description": activity_description,
                    "activity_date": activity_date.isoformat() if activity_date else None,
                    "start_time": start_time.strftime('%H:%M:%S') if start_time else None,
                    "end_time": end_time.strftime('%H:%M:%S') if end_time else None,
                    "cost": cost,
                    "destination_id": destination_id,
                    "site_type": site_type,
                    "site_description": site_description
                }
                response = add_sightseeing_activity(sightseeing_data)
                if response.status_code == 201:
                    st.success('Sightseeing activity added successfully.')
                    time.sleep(1)
                    st.experimental_rerun()
                else:
                    st.error('Failed to add sightseeing activity.')


def add_adventure_sport_activity_form(destination_options):
    with st.form("add_adventure_sport_activity_form", clear_on_submit=True):
        st.subheader("Add Adventure Sport Activity")
        destination_id = st.selectbox('Select Destination ID', destination_options)
        activity_location = st.text_input('Activity Location')
        activity_description = st.text_area('Activity Description')
        activity_date = st.date_input('Activity Date', None)
        start_time = st.time_input('Start Time', None)
        end_time = st.time_input('End Time', None)
        cost = st.number_input('Cost', step=10)
        sport_type = st.text_input('Sport Type')
        minimum_age = st.number_input('Minimum Age', min_value=0)
        other_restrictions = st.text_area('Other Restrictions')
        submit_button = st.form_submit_button('Add Adventure Sport Activity')

        if submit_button:
            if not sport_type or not minimum_age:
                st.error("Sport Type and Minimum Age Restrictions can't be empty for adding Adventure Sport Activity.")
            else:
                adventure_sport_data = {
                    "activity_location": activity_location,
                    "activity_description": activity_description,
                    "activity_date": activity_date.isoformat() if activity_date else None,
                    "start_time": start_time.strftime('%H:%M:%S') if start_time else None,
                    "end_time": end_time.strftime('%H:%M:%S') if end_time else None,
                    "cost": cost,
                    "destination_id": destination_id,
                    "sport_type": sport_type,
                    "min_age": minimum_age,
                    "restrictions": other_restrictions
                }
                response = add_adventure_sport_activity(adventure_sport_data)
                if response.status_code == 201:
                    st.success('Adventure sport activity added successfully.')
                    time.sleep(1)
                    st.experimental_rerun()
                else:
                    st.error('Failed to add adventure sport activity.')


def add_other_activity_form(destination_options):
    with st.form("add_other_activity_form", clear_on_submit=True):
        st.subheader("Add Activity")
        destination_id = st.selectbox('Select Destination ID', destination_options)
        activity_location = st.text_input('Activity Location')
        activity_description = st.text_area('Activity Description')
        activity_date = st.date_input('Activity Date', None)
        start_time = st.time_input('`Start Time`', None)
        end_time = st.time_input('End Time', None)
        cost = st.number_input('Cost', step=10)
        submit_button = st.form_submit_button('Add Activity')

        if submit_button:
            other_activity_data = {
                "activity_location": activity_location,
                "activity_description": activity_description,
                "activity_date": activity_date.isoformat() if activity_date else None,
                "start_time": start_time.strftime('%H:%M:%S') if start_time else None,
                "end_time": end_time.strftime('%H:%M:%S') if end_time else None,
                "cost": cost,
                "destination_id": destination_id
            }
            response = add_activity(other_activity_data)
            if response.status_code == 201:
                st.success('Activity added successfully.')
                time.sleep(1)
                st.experimental_rerun()
            else:
                st.error('Failed to add activity.')


def display_essential_items():
    st.subheader("Essential Items")
    if 'user_email' in st.session_state:
        trips_df, error = fetch_trips(st.session_state['user_email'])
        if not trips_df.empty:
            trip_options = list(trips_df['Trip Id'])
            selected_trip_id = st.selectbox('Select a Trip ID to manage essential items', trip_options)

            essential_items, error = fetch_essential_items(selected_trip_id)
            if essential_items:
                items_df = pd.DataFrame(essential_items)
                st.dataframe(items_df)

                with st.expander("Delete Essential Item"):
                    item_ids = items_df['item_id'].tolist()
                    selected_item_id = st.selectbox("Select an Item ID to delete", item_ids)
                    if st.button('Delete Item'):
                        response = delete_essential_items(selected_trip_id, selected_item_id)
                        if response.status_code == 200:
                            st.success("Item deleted successfully.")
                            st.experimental_rerun()
                        else:
                            st.error(f"Failed to delete item. Error: {response.json().get('error')}")
            else:
                st.error(error or "No essential items found for the selected trip.")

            with st.expander("Add Essential Item"):
                with st.form("add_essential_item_form", clear_on_submit=True):
                    item_name = st.text_input("Item Name")
                    submit_button = st.form_submit_button("Add Item")

                    if submit_button:
                        essential_item_data = {
                            "item_name": item_name,
                            "trip_id": selected_trip_id
                        }
                        response = create_essential_items(essential_item_data)
                        if response.status_code == 201:
                            st.success("Item added successfully.")
                            st.experimental_rerun()
                        else:
                            st.error(f"Failed to add item. Error: {response.json().get('error')}")

    else:
        st.error("Please log in to view and manage essential items.")


def display_all_trips_without_procedures():
    trips_df, error = fetch_all_trips()
    if not trips_df.empty:
        fig_cost_dist = px.box(
            trips_df,
            x='Destination Name',
            y='Cost',
            color='Destination Name',
            title='Cost Distribution by Destination'
        )
        st.plotly_chart(fig_cost_dist)
        activities_per_destination = trips_df.groupby('Destination Name').size().reset_index(name='Activities Count')
        fig_activities_destination = px.scatter(
            activities_per_destination,
            x='Destination Name',
            y='Activities Count',
            size='Activities Count',
            title='Number of Activities per Destination'
        )
        trip_status_counts = trips_df['Trip Status'].value_counts().reset_index()
        trip_status_counts.columns = ['Trip Status', 'Count']
        fig_status_counts = px.bar(
            trip_status_counts,
            x='Trip Status',
            y='Count',
            title='Count of Trips by Status'
        )
        st.plotly_chart(fig_status_counts)
        st.plotly_chart(fig_activities_destination)
        fig_activity_costs = px.histogram(
            trips_df,
            x='Cost',
            title='Distribution of Activity Costs'
        )
        st.plotly_chart(fig_activity_costs)
        trip_status_fig = px.bar(
            x=trips_df['Trip Status'].value_counts().index,  # Using the index as x-values
            y=trips_df['Trip Status'].value_counts().values,  # Using the counts as y-values
            title='Count of Trips by Status',
            labels={'x': 'Trip Status', 'y': 'Count'}
        )
        st.plotly_chart(trip_status_fig)
        st.subheader("Trip Details")
        st.dataframe(trips_df)
    else:
        st.error(error or "No trips available.")


def display_all_trips_with_procedures():
    st.subheader("All Trips Overview")

    average_cost_url = f"{FLASK_SERVER_URL}/averageActivityCostByCountry"
    packing_items_url = f"{FLASK_SERVER_URL}/commonPackingItems"
    popularity_url = f"{FLASK_SERVER_URL}/destinationPopularityOverTime"
    accommodation_choices_url = f"{FLASK_SERVER_URL}/getAccommodationChoices"

    average_cost_response = requests.get(average_cost_url).json()
    packing_items_response = requests.get(packing_items_url).json()
    popularity_response = requests.get(popularity_url).json()
    accommodation_choices_response = requests.get(accommodation_choices_url).json()

    average_cost_df = pd.DataFrame(average_cost_response['get_average_activity_cost_by_country'])
    packing_items_df = pd.DataFrame(packing_items_response['common_packing_items'])
    popularity_df = pd.DataFrame(popularity_response['destination_popularity'])
    accommodation_choices_df = pd.DataFrame(accommodation_choices_response['accommodations'])

    if not average_cost_df.empty:
        fig_avg_cost = px.bar(
            average_cost_df,
            x='country',
            y='average_cost',
            title='Average Activity Cost by Country'
        )
        st.plotly_chart(fig_avg_cost)

    if not packing_items_df.empty:
        fig_packing_items = px.bar(
            packing_items_df,
            x='item_name',
            y='item_count',
            title='Most Common Packing Items'
        )
        st.plotly_chart(fig_packing_items)


    if not accommodation_choices_df.empty:
        accommodation_choices_df['duration'] = pd.to_numeric(accommodation_choices_df['duration'], errors='coerce')
        accommodation_choices_df['booking_count'] = pd.to_numeric(accommodation_choices_df['booking_count'],
                                                                  errors='coerce')

        fig_accommodation_choices = px.scatter(
            accommodation_choices_df,
            x='accommodation_name',
            y='duration',
            size='booking_count',
            color='accommodation_name',
            title='Accommodation Choices by Travel Duration',
            labels={'duration': 'Duration (days)', 'booking_count': 'Number of Bookings'}
        )
        st.plotly_chart(fig_accommodation_choices)

    if average_cost_df.empty and packing_items_df.empty and popularity_df.empty and accommodation_choices_df.empty:
        st.error("No data available for visualizations.")


if __name__ == "__main__":
    main()
