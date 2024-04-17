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


def add_activity(activity_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addActivity", json=activity_data)
    return response


def add_sightseeing_activity(sightseeing_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addSightSeeingActivity", json=sightseeing_data)
    return response


def add_adventure_sport_activity(adventure_sport_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addAdventureSportActivity", json=adventure_sport_data)
    return response


def delete_activity(activity_id):
    response = requests.delete(f"{FLASK_SERVER_URL}/deleteActivity/{activity_id}")
    return response


def fetch_expenses(trip_ids):
    # Ensure trip_ids is a list even if a single ID is provided
    if not isinstance(trip_ids, list):
        trip_ids = [trip_ids]

    response = requests.post(f"{FLASK_SERVER_URL}/getExpensesByTripIds", json={"trip_ids": trip_ids})
    if response.status_code == 200:
        return response.json()['expenses'], None
    else:
        return [], "Failed to fetch expenses."


def create_expense(expense_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addExpense", json=expense_data)
    return response


def delete_expense(expense_id):
    response = requests.delete(f"{FLASK_SERVER_URL}/deleteExpense/{expense_id}")
    return response


def fetch_essential_items(trip_ids):
    if not isinstance(trip_ids, list):
        trip_ids = [trip_ids]

    response = requests.post(f"{FLASK_SERVER_URL}/getItemsByTripIds", json={"trip_ids": trip_ids})
    if response.status_code == 200:
        return response.json()['items'], None
    else:
        return [], "Failed to fetch essential items."


def create_essential_items(essential_items_data):
    response = requests.post(f"{FLASK_SERVER_URL}/addItemToTrip", json=essential_items_data)
    return response


def delete_essential_items(trip_id, essential_items_id):
    response = requests.delete(f"{FLASK_SERVER_URL}/deleteItem/{trip_id}/{essential_items_id}")
    return response

def update_trip(trip_id, trip_update_data):
    # You need to implement this function according to your API's requirements
    response = requests.put(f"{FLASK_SERVER_URL}/updateTrip/{trip_id}", json=trip_update_data)
    return response.ok

def update_user_info(user_info, email_id):
    # You need to implement this function according to your API's requirements
    response = requests.put(f"{FLASK_SERVER_URL}/updateTraveller/{email_id}", json=user_info)
    return response.ok

def update_destination_info(destination_update_data):
    # You need to implement this function according to your API's requirements
    response = requests.put(f"{FLASK_SERVER_URL}/updateDestination/{destination_update_data['destination_id']}", json=destination_update_data)
    return response.ok

def fetch_all_trips():
    response = requests.get(f"{FLASK_SERVER_URL}/allTrips")
    if response.status_code == 200:
        trips_data = response.json()  # Assuming the JSON response is directly a list of dictionaries
        trips_df = pd.DataFrame(trips_data)
        return trips_df, None
    else:
        return pd.DataFrame(), "Failed to fetch all trips."