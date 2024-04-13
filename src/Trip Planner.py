import streamlit as st
from streamlit_option_menu import option_menu

from rest_api import *

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
        password = st.text_input('Password', type='password')
        mobile = st.text_input('Mobile')
        fname = st.text_input('First Name')
        lname = st.text_input('Last Name')
        gen = st.text_input('Gender')
        dob = st.date_input('Date of Birth')
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
                    'password': password,
                    'mobile': mobile,
                    'fname': fname,
                    'lname': lname,
                    'gen': gen,
                    'dob': dob.isoformat(),  # converting date to string
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


def display_trips():
    st.subheader("Your Trips")
    if 'user_email' in st.session_state:
        trips_df, error = fetch_trips(st.session_state['user_email'])

        if not trips_df.empty:
            # Assuming the last 4 columns are 'trip_name', 'start_date', 'end_date', 'trip_status'
            # and they are in the correct order in the DataFrame
            trips_df = trips_df.iloc[:, -4:]  # Select only the last 4 columns

            # Now rename the columns to have more readable names
            # The order should match the last 4 columns in your DataFrame
            trips_df.columns = ['Trip Name', 'Start Date', 'End Date', 'Status']

            # Ensure dates are in the correct format, assuming they are not already
            trips_df['Start Date'] = pd.to_datetime(trips_df['Start Date']).dt.strftime('%Y-%m-%d')
            trips_df['End Date'] = pd.to_datetime(trips_df['End Date']).dt.strftime('%Y-%m-%d')

            # Display the DataFrame using st.table to keep the headers fixed
            st.table(trips_df)
        else:
            st.error(error or "No trips found.")


def main():
    st.title('Travel Itinerary App')
    options = ["Home", "Sign Up", "Login"]
    icons = ["house", "person-plus", "door-open"]

    if 'user_email' in st.session_state:
        options += ["Your Trips", "Logout"]
        options.remove("Sign Up")
        options.remove("Login")
        icons += ["map", "box-arrow-right"]

    selected = option_menu("Main Menu", options, icons=icons, menu_icon="cast", default_index=0,
                           orientation="horizontal")

    if selected == "Home":
        if 'f_name' in st.session_state:
            name = st.session_state['f_name']
        else:
            name = 'Traveller'
        st.subheader("Hi " + name + "! Welcome to the Travel Itinerary App!")
    elif selected == "Sign Up":
        signup_page()
    elif selected == "Login":
        login_page()
    elif selected == "Your Trips" and 'user_email' in st.session_state:
        display_trips()
    elif selected == "Logout":
        if 'user_email' in st.session_state:
            del st.session_state['user_email']
        st.rerun()  # Re-run to update the UI and navigation options


if __name__ == "__main__":
    main()
