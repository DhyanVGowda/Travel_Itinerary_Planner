from decimal import Decimal
from flask import Flask, Response, jsonify, request
import json
import datetime
import pymysql
from pymysql.err import Error


# After creating the Flask app


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, datetime.time):
            return obj.strftime('%H:%M:%S')
        elif isinstance(obj, datetime.timedelta):
            return obj.total_seconds()
        elif isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)


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


@app.route('/trips/<email>', methods=['GET'])
def get_trips(email):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetTripsByTravellerEmail', [email])
        trips_raw = cursor.fetchall()
        # Assuming you know the column names or using cursor.description to get them
        columns = [col[0] for col in cursor.description]
        trips = [dict(zip(columns, trip)) for trip in trips_raw]
    except Error as e:
        print("Failed to retrieve trips: ", e)
        return jsonify({'error': 'Failed to retrieve trips'}), 500
    finally:
        cursor.close()
    if trips:
        return jsonify({"trips": trips}), 200
    else:
        return jsonify({"trips": []}), 200


@app.route('/getDestinationsByTripIds', methods=['POST'])
def get_destinations():
    data = request.get_json()
    try:
        trips = data.get('trip_ids')
        cursor = connection.cursor()
        sql = ("SELECT thd.trip_id, d.* "
               "FROM Destination d "
               "INNER JOIN Trip_Has_Destination thd "
               "ON thd.destination_id = d.destination_id "
               f"WHERE thd.trip_id IN ({', '.join(map(str, trips))}) ORDER BY trip_id;")
        cursor.execute(sql)
        result = cursor.fetchall()
        destinations = [dict(zip([column[0] for column in cursor.description], row)) for row in result]
        destinations_json = json.dumps({'destinations': destinations}, cls=CustomEncoder)
        return destinations_json, 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


def check_empty(value):
    if value == '':
        return None
    return value


@app.route('/createTrip', methods=['POST'])
def create_trip_details():
    data = request.get_json()
    print(data)
    email = data.get('email')
    trip_name = data.get('trip_name')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    status = data.get('status')

    try:
        with connection.cursor() as cursor:

            connection.begin()

            cursor.callproc('AddTrip', [trip_name, start_date, end_date, status])

            cursor.execute("SELECT LAST_INSERT_ID()")
            trip_id = cursor.fetchone()[0]

            cursor.callproc('AddTravellerTripPlan', [email, trip_id])

            connection.commit()

            return jsonify({'message': 'Trip and traveler\'s trip plan added successfully'}), 201
    except Error as e:
        print("Failed to add trip and traveler's trip plan:", e)
        connection.rollback()
        return jsonify({'error': 'Failed to add trip and traveler\'s trip plan'}), 500


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
        cursor.callproc('AddTraveller',
                        [email, mobile, fname, lname, gen, dob, unit, street, street_no, city, state, zip_code])
        connection.commit()
        return jsonify({'message': 'Signup successful'}), 201
    except pymysql.err.InternalError as e:
        connection.rollback()
        if e.args[0] == 1644:
            return jsonify({'error': e.args[1]}), 400
        else:
            return jsonify({'error': 'Signup failed due to database error'}), 500
    except pymysql.Error as e:
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addOtherTravellerToTrip', methods=['POST'])
def add_other_traveller():
    try:
        data = request.json
        email = data.get('email')
        trip_id = data.get('trip_id')
        cursor = connection.cursor()
        sql = "INSERT INTO traveller_plans_trip (email_id, trip_id) VALUES (%s, %s)"
        cursor.execute(sql, (email, trip_id))
        connection.commit()
        return jsonify({'message': 'Traveller Added Successfully'}), 201
    except Error as e:
        if 'Duplicate entry' in str(e):
            return jsonify({'error': 'Traveller Already a Part of the Trip'}), 500
        elif 'foreign key constraint' in str(e):
            return jsonify({'error': 'Cannot Find traveller'}), 501
        else:
            return jsonify({'error': str(e)}), 502
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
                print("Login successful")
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


@app.route('/deleteTrip/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteTripById', [trip_id])
        connection.commit()
        return jsonify({'message': 'Trip deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete trip: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/getAccomodationHomeStayByTripIds', methods=['POST'])
def get_accommodation_homestay():
    data = request.get_json()
    try:
        trips = data.get('trip_ids')
        cursor = connection.cursor()
        sql = ("SELECT thd.trip_id, ah.* "
               "FROM Accommodation_HomeStay ah "
               "INNER JOIN Trip_Has_Destination thd "
               "ON thd.destination_id = ah.destination_id "
               f"WHERE thd.trip_id IN ({', '.join(map(str, trips))}) ORDER BY thd.trip_id, thd.destination_id;")
        cursor.execute(sql)
        result = cursor.fetchall()
        accommodation_homestays = [dict(zip([column[0] for column in cursor.description], row)) for row in result]
        accommodation_homestays_json = json.dumps({'accommodation_homestays': accommodation_homestays},
                                                  cls=CustomEncoder)
        return accommodation_homestays_json, 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getAccomodationHostelByTripIds', methods=['POST'])
def get_accommodation_hostel():
    data = request.get_json()
    try:
        trips = data.get('trip_ids')
        cursor = connection.cursor()
        sql = ("SELECT thd.trip_id, ah.* "
               "FROM Accommodation_Hostel ah "
               "INNER JOIN Trip_Has_Destination thd "
               "ON thd.destination_id = ah.destination_id "
               f"WHERE thd.trip_id IN ({', '.join(map(str, trips))}) ORDER BY thd.trip_id, thd.destination_id;")
        cursor.execute(sql)
        result = cursor.fetchall()
        accommodation_hostel = [dict(zip([column[0] for column in cursor.description], row)) for row in result]
        accommodation_hostel_json = json.dumps({'accommodation_hostels': accommodation_hostel},
                                               cls=CustomEncoder)
        return accommodation_hostel_json, 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getAccomodationHotelByTripIds', methods=['POST'])
def get_accommodation_hotel():
    data = request.get_json()
    try:
        trips = data.get('trip_ids')
        cursor = connection.cursor()
        sql = ("SELECT thd.trip_id, ah.* "
               "FROM Accommodation_Hotel ah "
               "INNER JOIN Trip_Has_Destination thd "
               "ON thd.destination_id = ah.destination_id "
               f"WHERE thd.trip_id IN ({', '.join(map(str, trips))}) ORDER BY thd.trip_id, thd.destination_id;")
        cursor.execute(sql)
        result = cursor.fetchall()
        accommodation_hotel = [dict(zip([column[0] for column in cursor.description], row)) for row in result]
        accommodation_hotel_json = json.dumps({'accommodation_hotels': accommodation_hotel},
                                              cls=CustomEncoder)
        return accommodation_hotel_json, 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getActivityByTripIds', methods=['POST'])
def get_activity():
    data = request.get_json()
    try:
        trips = data.get('trip_ids')
        cursor = connection.cursor()
        sql = ("SELECT td.trip_id, t.trip_name, d.destination_name, "
               "a.activity_id, a.activity_location, a.activity_description, "
               "a.activity_date, a.start_time, a.end_time, a.cost, "
               "ss.site_type, ss.site_description, "
               "asp.sport_type, asp.minimum_age, asp.other_restrictions "
               "FROM Activity a "
               "LEFT JOIN Activity_SightSeeing ss ON a.activity_id = ss.activity_id "
               "LEFT JOIN Activity_AdventureSport asp ON a.activity_id = asp.activity_id "
               "INNER JOIN Trip_Has_Destination td ON a.destination_id = td.destination_id "
               "INNER JOIN Trip t ON td.trip_id = t.trip_id "
               "INNER JOIN Destination d ON td.destination_id = d.destination_id "
               f"WHERE td.trip_id IN ({', '.join(map(str, trips))})")
        cursor.execute(sql)
        result = cursor.fetchall()
        activities = [dict(zip([column[0] for column in cursor.description], row)) for row in result]
        activities_json = json.dumps({'activities': activities}, cls=CustomEncoder)
        return activities_json, 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


if __name__ == '__main__':
    username = "root"
    password = "parrvaltd118"
    connection = connect_to_database(username, password)
    if connection is not None:
        app.run(debug=True)
    else:
        print("Cant connect to db")
        exit(-1)
