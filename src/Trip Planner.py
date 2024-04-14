import time

import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
from rest_api import *

import base64
from io import BytesIO

# Constants for Flask server
FLASK_SERVER_URL = "http://127.0.0.1:5000"


def signup_user(signup_data):
    response = requests.post(f"{FLASK_SERVER_URL}/signup", json=signup_data)
    return response


def login_user(login_data):
    response = requests.post(f"{FLASK_SERVER_URL}/login", json=login_data)
    return response


def fetch_trips(email):
    response = requests.get(f"{FLASK_SERVER_URL}/trips/{email}")
    if response.status_code == 200:
        return pd.DataFrame(response.json()), None  # Ensure to return None for error if successful
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
            trips_df_1 = trips_df.iloc[:, -4:]

            trips_df_1.columns = ['Trip Name', 'Start Date', 'End Date', 'Status']

            trips_df_1['Start Date'] = pd.to_datetime(trips_df_1['Start Date']).dt.strftime('%Y-%b-%d')
            trips_df_1['End Date'] = pd.to_datetime(trips_df_1['End Date']).dt.strftime('%Y-%b-%d')

            st.table(trips_df_1)

            export_format = st.radio("Export Format", ("CSV", "Excel"))
            if export_format == "CSV":
                st.download_button("Download CSV", trips_df.to_csv(), "trips.csv", "text/csv")
            elif export_format == "Excel":
                st.download_button("Download Excel", trips_df.to_excel(), "trips.xlsx",
                                   "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

            # Add functionality to delete a trip
            delete_trip_index = st.selectbox('Select a trip to delete (by index)', trips_df.index)
            if st.button('Delete Trip'):
                trip_id_to_delete = trips_df.loc[delete_trip_index, 'Trip ID']  # Replace with actual ID column name
                response = delete_trip(trip_id_to_delete)
                if response.status_code == 200:
                    st.success(f"Trip {trip_id_to_delete} deleted successfully.")
                    st.experimental_rerun()
                else:
                    st.error('Failed to delete the trip.')

        else:
            st.error(error or "No trips found.")

    # Interface to add a new trip
    st.subheader('Add New Trip')
    with st.form("add_trip_form"):
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
            st.sidebar.write(f"**Mobile:** {user_info[1]}")              # Index for mobile
            st.sidebar.write(f"**Address:** {user_info[7]} {user_info[8]}")  # Index for unit and street
            st.sidebar.write(f"**City:** {user_info[9]}")                 # Index for city
            st.sidebar.write(f"**State:** {user_info[10]}")                # Index for state
        else:
            # If there is no user info or an empty response, display an error message
            st.sidebar.error("Failed to load traveler information.")
    else:
        # If there is no email in the session state, prompt the user to log in
        st.sidebar.write("Please log in to see traveler information.")



def main():
    st.title('Travel Itinerary App')

    # Sidebar menu
    options = ["Home", "Sign Up", "Login"]
    icons = ["house", "person-plus", "door-open"]

    # If user is logged in, show their info in the sidebar
    if 'user_email' in st.session_state:
        show_user_info()
        options += ["Your Trips", "Logout"]
        options.remove("Sign Up")
        options.remove("Login")
        icons += ["map", "box-arrow-right"]

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
    elif selected == "Your Trips" and 'user_email' in st.session_state:
        display_trips()
    elif selected == "Logout":
        for key in ['user_email', 'user_info']:
            if key in st.session_state:
                del st.session_state[key]
        st.experimental_rerun()


if __name__ == "__main__":
    main()