from flask import Flask, request, jsonify
import pymysql
from pymysql import Error

app = Flask(__name__)


def connect_to_database(username, password):
    try:
        return pymysql.connect(host='localhost',
                               user=username,
                               password=password,
                               database='travel_itinerary',
                               charset='utf8mb4')

    except pymysql.Error as e:
        code, msg = e.args
        print("Cannot connect to the database", code, msg)


def call_addtraveller(connection, email, mobile, fname, lname, gen, dob, unit, street, street_no, city, state, zip):
    try:
        cursor = connection.cursor()
        cursor.callproc('AddTraveller',
                        [email, mobile, fname, lname, gen, dob, unit, street, street_no, city, state, zip])
        connection.commit()
        print("Traveller added successfully.")
        return True
    except Error as e:
        print("Failed to add traveller: ", e)
        return False
    finally:
        cursor.close()


@app.route('/trips/<email>', methods=['GET'])
def get_trips(email):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetTripsByTravellerEmail', [email])
        trips = cursor.fetchall()
    except Error as e:
        print("Failed to retrieve trips: ", e)
        return jsonify({'error': 'Failed to retrieve trips'}), 500
    finally:
        cursor.close()
    if trips:
        return jsonify(trips), 200

def check_empty(value):
    if value == '':
        return None
    return value


@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    mobile = data.get('mobile')
    fname = data.get('fname')

    lname = check_empty(data.get('lname'))
    gen = check_empty(data.get('gen'))
    dob = check_empty(data.get('dob'))
    unit = check_empty(data.get('unit'))
    street = check_empty(data.get('street'))
    street_no = check_empty(data.get('street_no'))
    city = check_empty(data.get('city'))
    state = check_empty(data.get('state'))
    zip_code = check_empty(data.get('zip'))

    try:
        cursor = connection.cursor()
        cursor.callproc('AddTraveller', [email, mobile, fname, lname, gen, dob, unit, street, street_no, city, state,
                                         zip_code])
        connection.commit()
        return jsonify({'message': 'Signup successful'}), 201
    except Error as e:
        connection.rollback()
        print("Failed to sign up traveller: ", str(e))
        return jsonify({'error': 'Signup failed due to database error'}), 500
    finally:
        cursor.close()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email:
        return jsonify({'error': 'Email is required'}), 400

    if not password:
        return jsonify({'error': 'Password is required'}), 400

    try:
        cursor = connection.cursor()
        cursor.callproc('GetTravellerByEmail', [email])
        traveller = cursor.fetchone()
        if traveller:
            phone_number = traveller[1]
            if phone_number == password:
                print("Login successful!")
                print("Traveller Details:")
                return jsonify(traveller), 200
            else:
                return jsonify({'error': 'Incorrect password'}), 401
        else:
            return jsonify({'error': 'No traveller found with the provided email'}), 404
    except Error as e:
        print("Failed to retrieve traveller: ", str(e))
        return jsonify({'error': 'Database error'}), 500
    finally:
        cursor.close()


if __name__ == '__main__':
    username = "root"
    password = "parrvaltd118"
    connection = connect_to_database(username, password)
    app.run(debug=True)
