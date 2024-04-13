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

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    email = data['email']
    password = data['password']
    mobile = data['mobile']
    fname = data['fname']
    lname = data['lname']
    gen = data['gen']
    dob = data['dob']
    unit = data['unit']
    street = data['street']
    street_no = data['street_no']
    city = data['city']
    state = data['state']
    zip_code = data['zip']

    success = call_addtraveller(connection, email, mobile, fname, lname, gen, dob, unit, street, street_no, city, state,
                                zip_code)

    if success:
        return jsonify({'message': 'Signup successful'}), 201
    else:
        return jsonify({'error': 'Signup failed'}), 400


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    #valid = call_gettravellerbyemail(email, password)
    try:
        cursor = connection.cursor()
        cursor.callproc('GetTravellerByEmail', [email])
        valid = False
        traveller = cursor.fetchone()
        phone_number = traveller[1]
        if traveller:
            if phone_number == password:
                print("Login successful!")
                print("Traveller Details:")
                columns = [desc[0] for desc in cursor.description]
                valid = True
            else:
                print("Incorrect password.")
        if not valid:
            print("Login failed. Incorrect email or password.")
        return valid
    except Error as e:
        print("Failed to retrieve traveller: ", e)
        return False
    finally:
        cursor.close()

    if valid:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Login failed. Incorrect email or password'}), 401


if __name__ == '__main__':
    username = "root"
    password = "parrvaltd118"
    connection = connect_to_database(username, password)
    app.run(debug=True)
