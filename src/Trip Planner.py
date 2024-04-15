import time
from io import BytesIO

import streamlit as st
from streamlit_option_menu import option_menu

from rest_api import *


def signup_user(signup_data):
    response = requests.post(f"{FLASK_SERVER_URL}/signup", json=signup_data)
    return response


def login_user(login_data):
    response = requests.post(f"{FLASK_SERVER_URL}/login", json=login_data)
    return response


def fetch_trips(email):
    response = requests.get(f"{FLASK_SERVER_URL}/trips/{email}")
    if response.status_code == 200:
        # The JSON response is expected to be a dictionary with 'trips' as a key,
        # where 'trips' is a list of dictionaries representing each trip.
        trips_data = response.json().get("trips", [])  # Default to an empty list if "trips" key is absent
        trips_df = pd.DataFrame(trips_data)
        if not trips_df.empty:
            trips_df['start_date'] = pd.to_datetime(trips_df['start_date'], format='mixed')
            trips_df['end_date'] = pd.to_datetime(trips_df['end_date'], format='mixed')

            trips_df_1 = pd.DataFrame()
            trips_df_1['Trip Id'] = trips_df['trip_id']
            trips_df_1['Trip Name'] = trips_df['trip_name']
            trips_df_1['Trip Status'] = trips_df['trip_status']
            trips_df_1['Start Date'] = trips_df['start_date'].dt.strftime('%Y-%b-%d')
            trips_df_1['End Date'] = trips_df['end_date'].dt.strftime('%Y-%b-%d')
            return trips_df_1, None  # Convert the list of dictionaries to a DataFrame
        else:
            return pd.DataFrame(), "No Trips found."
    else:
        return pd.DataFrame(), "Failed to fetch trips."  # Return an empty DataFrame and an error message


def signup_page():
    with st.form("signup_form"):
        st.subheader('Sign Up')
        email = st.text_input('Email')
        mobile = st.text_input('Mobile')
        fname = st.text_input('First Name')
        lname = st.text_input('Last Name')
        gen = st.text_input('Gender')
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
                    st.success('Signup successful')
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


def update_trip(trip_update_data):
    # You need to implement this function according to your API's requirements
    response = requests.post(f"{FLASK_SERVER_URL}/updateTrips", json=trip_update_data)
    return response.ok


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data


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
                    trip_options = list(trips_df['Trip Id'])
                    selected_trip_id = st.selectbox('Select Trip ID', trip_options)
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
                trip_options = list(trips_df['Trip Id'])
                selected_trip_id = st.selectbox('Select Trip ID', trip_options)
                if st.button('Delete Trip'):
                    response = delete_trip(selected_trip_id)
                    if response.status_code == 200:
                        st.success(f"Trip deleted successfully.")
                        time.sleep(1)
                        st.experimental_rerun()
                    else:
                        st.error('Failed to delete the trip.')

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
                    'status': new_status
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
            st.sidebar.write(f"**Address:** {user_info[7]} {user_info[8]}")  # Index for unit and street
            st.sidebar.write(f"**City:** {user_info[9]}")  # Index for city
            st.sidebar.write(f"**State:** {user_info[10]}")  # Index for state
        else:
            # If there is no user info or an empty response, display an error message
            st.sidebar.error("Failed to load traveler information.")
    else:
        # If there is no email in the session state, prompt the user to log in
        st.sidebar.write("Please log in to see traveler information.")


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
            trip_ids = trips_df['Trip Id'].tolist()  # Assuming 'Trip Id' is the correct column name
            destinations_df, error = get_destinations(trip_ids)
            if not destinations_df.empty:
                st.dataframe(destinations_df)

                with st.expander("Delete Destinations"):
                    trip_options = list(destinations_df['trip_id'])
                    selected_trip_id = st.selectbox('Select Trip Id', trip_options)
                    destinations_options = list(destinations_df['destination_id'])
                    selected_destn_id = st.selectbox('Select Destination Id', destinations_options)
                    if st.button('Delete Destination'):
                        response = delete_destination(selected_trip_id, selected_destn_id)
                        if response.status_code == 200:
                            st.success(f"Destination deleted successfully.")
                            time.sleep(1)
                            st.experimental_rerun()
                        else:
                            st.error('Failed to delete the Destination.' + response.json().get('error'))
            else:
                st.error(error or "No destinations found.")

            with st.form("add_destination_form", clear_on_submit=True):
                st.subheader("Add Destination to Trip")
                trip_options = list(trips_df['Trip Id'])
                selected_trip_id = st.selectbox('Select Trip ID', trip_options)
                destination_name = st.text_input('Destination Name')
                country = st.text_input('Country')
                arrival_date = st.date_input('Arrival Date', None)
                departure_date = st.date_input('Departure Date', None)
                transport_mode = st.text_input('Transport Mode')
                travel_duration = st.text_input('Travel Duration')
                submit_button = st.form_submit_button('Add Destination')
                if submit_button:
                    if not destination_name or not country:
                        st.error('Destination name and country are required.')
                    else:
                        destination_data = {
                            "trip_id": selected_trip_id,
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
            trip_options = list(trips_df['Trip Id'])
            selected_trip_id = st.selectbox('Select a Trip ID to manage expenses', trip_options)

            expenses, error = fetch_expenses(selected_trip_id)
            if expenses:
                expenses_df = pd.DataFrame(expenses)
                st.dataframe(expenses_df)

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

    else:
        st.error("Please log in to view and manage expenses.")

def main():
    st.title('Travel Itinerary App')

    # Sidebar menu
    options = ["Home", "Sign Up", "Login"]
    icons = ["house", "person-plus", "door-open"]

    # If user is logged in, show their info in the sidebar
    if 'user_email' in st.session_state:
        show_user_info()
        options.remove("Sign Up")
        options.remove("Login")
        icons.remove("person-plus")
        icons.remove("door-open")
        options += ["Trips", "Destinations", "Activities", "Accommodations", "Expenses & Essential Items", "Logout"]
        icons += ["map", "globe", "biking", "hotel", "credit-card","box-arrow-right"]

    selected = option_menu("Main Menu", options, icons=icons, menu_icon="cast", default_index=0,
                           orientation="horizontal")

    if selected == "Home":
        st.subheader("Welcome to the Travel Itinerary App!")
        if 'user_email' in st.session_state:
            st.write("Logged in as:", st.session_state['user_email'])
    elif selected == "Sign Up":
        signup_page()
    elif selected == "Login":
        login_page()
    elif selected == "Trips" and 'user_email' in st.session_state:
        display_trips()
    elif selected == "Destinations" and 'user_email' in st.session_state:
        display_destinations()
    elif selected == "Activities" and 'user_email' in st.session_state:
        display_activities()
    elif selected == "Accommodations" and 'user_email' in st.session_state:
        display_accommodations()
    elif selected == "Expenses & Essential Items" and 'user_email' in st.session_state:
        display_expenses()
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
        destination_id = st.selectbox('Select Destination ID',  destination_options)
        activity_location = st.text_input('Activity Location')
        activity_description = st.text_area('Activity Description')
        activity_date = st.date_input('Activity Date', None)
        start_time = st.time_input('Start Time', None)
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


if __name__ == "__main__":
    main()
