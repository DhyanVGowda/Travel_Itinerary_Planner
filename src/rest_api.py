import requests
import pandas as pd

FLASK_SERVER_URL = "http://127.0.0.1:5000"


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
    response = requests.delete(f"{FLASK_SERVER_URL}/Trip/{trip_id}")
    return response


def get_destinations(trip_ids):
    response = requests.post(f"{FLASK_SERVER_URL}/getDestinationsByTripIds", json={'trip_ids': trip_ids})
    if response.status_code == 200:
        return pd.DataFrame(response.json().get('destinations')), None
    else:
        return pd.DataFrame(), "Failed to fetch destinations."
