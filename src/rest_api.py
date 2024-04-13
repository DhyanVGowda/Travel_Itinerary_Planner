import requests
import pandas as pd

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
        return pd.DataFrame(response.json())
    else:
        return pd.DataFrame(), "Failed to fetch trips."
