import streamlit as st
import requests

# Constants for Flask server
FLASK_SERVER_URL = "http://localhost:5000"

def signup_user(signup_data):
    response = requests.post(f"{FLASK_SERVER_URL}/signup", json=signup_data)
    return response

def login_user(login_data):
    response = requests.post(f"{FLASK_SERVER_URL}/login", json=login_data)
    return response

st.title('Travel Itinerary App')

with st.form('signup_form'):
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

with st.form('login_form'):
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
            st.success('Login successful')
        else:
            st.error('Login failed. Incorrect email or password.')