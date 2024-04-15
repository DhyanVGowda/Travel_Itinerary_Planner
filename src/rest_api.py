import json

import requests
import pandas as pd

with open('../configs.json', 'r') as file:
    configs = json.load(file)
FLASK_SERVER_URL = "http://127.0.0.1:" + configs["port"]


def signup_user(signup_data):
    response = requests.post(f"{FLASK_SERVER_URL}/signup", json=signup_data)
    return response


def login_user(login_data):
    response = requests.post(f"{FLASK_SERVER_URL}/login", json=login_data)
    return response


def add_traveller_to_trip(traveller_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addOtherTravellerToTrip", json=traveller_data)
    return response


def fetch_trips(email):
    response = requests.get(f"{FLASK_SERVER_URL}/trips/{email}")
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return pd.DataFrame(), "Failed to fetch trips."


def add_trip(trip_data):
    # Make a POST request to the add trip API endpoint
    response = requests.post(f"{FLASK_SERVER_URL}/createTrip", json=trip_data)
    print(response.status_code)
    return response


def delete_trip(trip_id):
    # Make a DELETE request to the delete trip API endpoint
    response = requests.delete(f"{FLASK_SERVER_URL}/deleteTrip/{trip_id}")
    return response


def get_destinations(trip_ids):
    response = requests.post(f"{FLASK_SERVER_URL}/getDestinationsByTripIds", json={'trip_ids': trip_ids})
    if response.status_code == 200:
        return pd.DataFrame(response.json().get('destinations')), None
    else:
        return pd.DataFrame(), "Failed to fetch destinations."


def get_accomodation_homestays(trip_ids):
    response = requests.post(f"{FLASK_SERVER_URL}/getAccomodationHomeStayByTripIds", json={'trip_ids': trip_ids})
    if response.status_code == 200:
        return pd.DataFrame(response.json().get('accommodation_homestays')), None
    else:
        return pd.DataFrame(), "Failed to fetch accomodations."


def get_accomodation_hostels(trip_ids):
    response = requests.post(f"{FLASK_SERVER_URL}/getAccomodationHostelByTripIds", json={'trip_ids': trip_ids})
    if response.status_code == 200:
        return pd.DataFrame(response.json().get('accommodation_hostels')), None
    else:
        return pd.DataFrame(), "Failed to fetch accomodations."


def get_accomodation_hotels(trip_ids):
    response = requests.post(f"{FLASK_SERVER_URL}/getAccomodationHotelByTripIds", json={'trip_ids': trip_ids})
    if response.status_code == 200:
        return pd.DataFrame(response.json().get('accommodation_hotels')), None
    else:
        return pd.DataFrame(), "Failed to fetch accomodations."


def get_activities(trip_ids):
    response = requests.post(f"{FLASK_SERVER_URL}/getActivityByTripIds", json={'trip_ids': trip_ids})
    if response.status_code == 200:
        return pd.DataFrame(response.json().get('activities')), None
    else:
        return pd.DataFrame(), "Failed to fetch activities."


def delete_destination(destination_id, trip_id):
    # Make a DELETE request to the delete trip API endpoint
    response = requests.delete(f"{FLASK_SERVER_URL}/deleteDestination/{trip_id}/{destination_id}")
    return response

def delete_homestay(accomodation_id):
    # Make a DELETE request to the delete trip API endpoint
    response = requests.delete(f"{FLASK_SERVER_URL}/deleteHomeStay/{accomodation_id}")
    return response

def delete_hostel(accomodation_id):
    # Make a DELETE request to the delete trip API endpoint
    response = requests.delete(f"{FLASK_SERVER_URL}/deleteHostel/{accomodation_id}")
    return response

def delete_hotel(accomodation_id):
    # Make a DELETE request to the delete trip API endpoint
    response = requests.delete(f"{FLASK_SERVER_URL}/deleteHotel/{accomodation_id}")
    return response

def add_destination_to_trip(destination_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addDestinationToTrip", json=destination_data)
    return response

def add_homestay(homestay_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addHomeStay", json=homestay_data)
    return response

def add_hotel(hotel_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addHotel", json=hotel_data)
    return response

def add_hostel(hostel_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addHostel", json=hostel_data)
    return response