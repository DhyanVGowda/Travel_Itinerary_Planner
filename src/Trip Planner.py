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
        else :
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
            else:
                st.error(error or "No Activity found.")
        else:
            st.error("No activity found to display.")
    else:
        st.error("Please log in to view Activities Data.")
    print(1)

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
                else:
                    st.error(error or "No homestay Accomodation found.")

                with st.expander("Delete Homestay"):
                    trip_options = list(homestay_df[''])
                    selected_homestay_id = st.selectbox('Select Homestay ID', trip_options)
                    if st.button('Delete Homestay'):
                        response = delete_homestay(selected_homestay_id)
                        if response.status_code == 200:
                            st.success(f"Homestay deleted successfully.")
                            time.sleep(1)
                            st.experimental_rerun()
                        else:
                            st.error('Failed to delete the Homestay.')
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
                else:
                    st.error(error or "No Hostel Accomodation found.")
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
                else:
                    st.error(error or "No Hotel Accomodation found.")
            else:
                st.error("No trips found to display.")
        else:
            st.error("Please log in to view accomodations.")


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
        options += ["Trips", "Destinations", "Activities", "Accommodations", "Logout"]
        icons += ["map", "globe", "biking", "hotel", "box-arrow-right"]

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
    elif selected == "Logout":
        for key in ['user_email', 'user_info']:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()


if __name__ == "__main__":
    main()
