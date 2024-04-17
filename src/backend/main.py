from decimal import Decimal
from time import time

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
            total_seconds = obj.total_seconds()
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{int(hours)}:{int(minutes)}:{int(seconds)}"
        elif isinstance(obj, Decimal):
            return str(obj)
        elif isinstance(obj, time):
            return obj.strftime('%H:%M:%S')
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
        sql = ("SELECT thd.trip_id,thd.transportation_mode,thd.travel_duration, d.* "
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


@app.route('/getExpensesByTripIds', methods=['POST'])
def get_expenses():
    data = request.get_json()
    try:
        trip_ids = data.get('trip_ids')
        cursor = connection.cursor()
        sql = ("SELECT * FROM Expense "
               f"WHERE trip_id IN ({', '.join(map(str, trip_ids))}) "
               "ORDER BY trip_id DESC, expense_date DESC;")
        cursor.execute(sql)
        result = cursor.fetchall()
        expenses = [dict(zip([column[0] for column in cursor.description], row)) for row in result]
        expenses_json = json.dumps({'expenses': expenses}, cls=CustomEncoder)
        return expenses_json, 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addExpense', methods=['POST'])
def add_expense():
    data = request.json
    exp_date = check_empty(data['expense_date'])
    exp_category = check_empty(data['expense_category'])
    exp_description = check_empty(data['expense_description'])
    amt = data['amount']
    curr = check_empty(data['currency'])
    trip = data['trip_id']
    try:
        cursor = connection.cursor()
        cursor.callproc('AddExpense', (exp_date, exp_category, exp_description, amt, curr, trip))
        # Commit the transaction
        connection.commit()
        return jsonify({'message': 'Expense added successfully'}), 201
    except Error as e:
        print("Failed to add an expense: ", str(e))
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


@app.route('/addDestinationToTrip', methods=['POST'])
def add_destination_to_trip():
    data = request.get_json()
    trip_id = data.get('trip_id')
    dest_name = data.get('destination_name')
    country = data.get('country')
    arrival_date = data.get('arrival_date')
    departure_date = data.get('departure_date')
    transport_mode = data.get('transport_mode')
    travel_duration = data.get('travel_duration')

    try:
        with connection.cursor() as cursor:
            connection.begin()

            # Create a new destination entry
            cursor.callproc('AddDestination', [dest_name, country, arrival_date, departure_date])

            # Get the destination ID
            cursor.execute("SELECT LAST_INSERT_ID()")
            dest_id = cursor.fetchone()[0]

            # Add the trip's destination
            cursor.callproc('AddTripDestination', [dest_id, trip_id, transport_mode, travel_duration])

            connection.commit()

            return jsonify({'message': 'Destination added to trip successfully'}), 201
    except Error as e:
        print("Failed to add destination to trip:", e)
        connection.rollback()
        return jsonify({'error': 'Failed to add destination to trip'}), 500


@app.route('/addItemToTrip', methods=['POST'])
def add_item_to_trip():
    data = request.get_json()
    trip_id = data.get('trip_id')
    item_name = data.get('item_name')
    try:
        with connection.cursor() as cursor:
            connection.begin()

            # Create a new destination entry
            cursor.callproc('AddEssentialPackingItem', [item_name])

            # Get the destination ID
            cursor.execute("SELECT LAST_INSERT_ID()")
            item_id = cursor.fetchone()[0]

            # Add the trip's essential item
            cursor.callproc('AddTripItem', [trip_id, item_id])

            connection.commit()

            return jsonify({'message': 'Item added to trip successfully'}), 201
    except Error as e:
        print("Failed to add destination to trip:", e)
        connection.rollback()
        return jsonify({'error': 'Failed to add item to trip'}), 500


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


@app.route('/addHomeStay', methods=['POST'])
def add_home_stay():
    data = request.json
    accommodation_name = data['accommodation_name']
    cost_per_night = data['cost_per_night']
    telephone_number = data['telephone_number']
    checkin_date = check_empty(data['checkin_date'])
    checkout_date = check_empty(data['checkout_date'])
    street_name = check_empty(data['street_name'])
    street_number = check_empty(data['street_number'])
    city = check_empty(data['city'])
    state = check_empty(data['state'])
    zipcode = check_empty(data['zipcode'])
    destination_id = data['destination_id']
    number_of_rooms = data['number_of_rooms']
    is_cook_available = check_empty(data['is_cook_available'])
    stay_type = check_empty(data['stay_type'])
    is_pet_allowed = check_empty(data['is_pet_allowed'])
    try:
        cursor = connection.cursor()
        cursor.callproc('AddHomeStayAccommodation', (accommodation_name, cost_per_night, telephone_number, checkin_date,
                                                     checkout_date, street_name, street_number, city, state, zipcode,
                                                     destination_id, number_of_rooms, is_cook_available, stay_type,
                                                     is_pet_allowed))

        # Commit the transaction
        connection.commit()
        return jsonify({'message': 'HomeStay Accommodation added successfully'}), 201
    except Error as e:
        print("Failed to add a  Homestay: ", str(e))
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addHotel', methods=['POST'])
def add_hotel():
    data = request.json
    accommodation_name = data['accommodation_name']
    cost_per_night = data['cost_per_night']
    telephone_number = data['telephone_number']
    checkin_date = check_empty(data['checkin_date'])
    checkout_date = check_empty(data['checkout_date'])
    street_name = check_empty(data['street_name'])
    street_number = check_empty(data['street_number'])
    city = check_empty(data['city'])
    state = check_empty(data['state'])
    zipcode = check_empty(data['zipcode'])
    destination_id = data['destination_id']
    number_of_rooms = data['number_of_rooms']
    meal = check_empty(data['meal'])
    star_rating = check_empty(data['star_rating'])
    try:
        cursor = connection.cursor()
        cursor.callproc('AddHotelAccommodation', (accommodation_name, cost_per_night, telephone_number, checkin_date,
                                                  checkout_date, street_name, street_number, city, state, zipcode,
                                                  destination_id, number_of_rooms, meal, star_rating))

        # Commit the transaction
        connection.commit()
        return jsonify({'message': 'Hotel Accommodation added successfully'}), 201
    except Error as e:
        print("Failed to add a Hotel: ", str(e))
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addHostel', methods=['POST'])
def add_hostel():
    data = request.json
    accommodation_name = data['accommodation_name']
    cost_per_night = data['cost_per_night']
    telephone_number = data['telephone_number']
    checkin_date = check_empty(data['checkin_date'])
    checkout_date = check_empty(data['checkout_date'])
    street_name = check_empty(data['street_name'])
    street_number = check_empty(data['street_number'])
    city = check_empty(data['city'])
    state = check_empty(data['state'])
    zipcode = check_empty(data['zipcode'])
    destination_id = data['destination_id']
    meal = check_empty(data['meal'])
    bath_type = check_empty(data['bath_type'])
    wifi = check_empty(data['wifi'])
    mixed_dorm = check_empty(data['mixed_dorm'])
    try:
        cursor = connection.cursor()
        cursor.callproc('AddHostelAccommodation', (accommodation_name, cost_per_night, telephone_number, checkin_date,
                                                   checkout_date, street_name, street_number, city, state, zipcode,
                                                   destination_id, meal, bath_type, wifi, mixed_dorm))

        # Commit the transaction
        connection.commit()
        return jsonify({'message': 'Hostel Accommodation added successfully'}), 201
    except Error as e:
        print("Failed to add a Hostel: ", str(e))
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addActivity', methods=['POST'])
def add_activity():
    data = request.json
    loc = data['activity_location']
    description = check_empty(data['activity_description'])
    act_date = data['activity_date']
    start_time = data['start_time']
    end_time = data['end_time']
    cst = check_empty(data['cost'])
    dest_id = data['destination_id']
    try:
        cursor = connection.cursor()
        cursor.callproc('AddActivity', (loc, description, act_date, start_time, end_time, cst, dest_id))
        # Commit the transaction
        connection.commit()
        return jsonify({'message': 'Activity added successfully'}), 201
    except Error as e:
        print("Failed to add an activity: ", str(e))
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addSightSeeingActivity', methods=['POST'])
def add_sightseeing_activity():
    data = request.json
    loc = data['activity_location']
    description = check_empty(data['activity_description'])
    act_date = data['activity_date']
    start_time = data['start_time']
    end_time = data['end_time']
    cst = check_empty(data['cost'])
    dest_id = data['destination_id']
    site_type = data['site_type']
    site_description = check_empty(data['site_description'])
    try:
        cursor = connection.cursor()
        cursor.callproc('AddActivity', (loc, description, act_date, start_time, end_time, cst, dest_id))
        # Call the AddSightseeingActivity procedure
        cursor.execute("SELECT LAST_INSERT_ID()")
        activity_id = cursor.fetchone()[0]
        cursor.callproc('AddSightseeingActivity', [activity_id, site_type, site_description])
        # Commit the transaction
        connection.commit()
        return jsonify({'message': 'SightSeeing Activity added successfully'}), 201
    except Error as e:
        print("Failed to add an activity: ", str(e))
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addAdventureSportActivity', methods=['POST'])
def add__activity():
    data = request.json
    loc = data['activity_location']
    description = check_empty(data['activity_description'])
    act_date = data['activity_date']
    start_time = data['start_time']
    end_time = data['end_time']
    cst = check_empty(data['cost'])
    dest_id = data['destination_id']
    sport_type = check_empty(data['sport_type'])
    min_age = check_empty(data['min_age'])
    restrictions = check_empty(data['restrictions'])
    try:
        cursor = connection.cursor()
        cursor.callproc('AddActivity', (loc, description, act_date, start_time, end_time, cst, dest_id))
        # Call the AddAdventureSportActivity procedure
        cursor.execute("SELECT LAST_INSERT_ID()")
        activity_id = cursor.fetchone()[0]
        cursor.callproc('AddAdventureSportActivity', [activity_id, sport_type, min_age, restrictions])
        # Commit the transaction
        connection.commit()
        return jsonify({'message': 'SightSeeing Activity added successfully'}), 201
    except Error as e:
        print("Failed to add an activity: ", str(e))
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

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


@app.route('/deleteExpense/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteExpenseById', [expense_id])
        connection.commit()
        return jsonify({'message': 'Expense deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete expense: ' + str(e)}), 500
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


@app.route('/getItemsByTripIds', methods=['POST'])
def get_items_by_trip_ids():
    data = request.get_json()
    try:
        trip_ids = data.get('trip_ids')
        cursor = connection.cursor()
        sql = ("SELECT tri.trip_id, e.* "
               "FROM Trip_Requires_Item tri "
               "INNER JOIN EssentialPackingItems e "
               "ON tri.item_id = e.item_id "
               f"WHERE tri.trip_id IN ({', '.join(map(str, trip_ids))});")
        cursor.execute(sql)
        result = cursor.fetchall()
        items = [dict(zip([column[0] for column in cursor.description], row)) for row in result]
        items_json = json.dumps({'items': items}, cls=CustomEncoder)
        return items_json, 200
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


@app.route('/deleteDestination/<int:trip_id>/<int:dest_id>', methods=['DELETE'])
def delete_destination(trip_id, dest_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteTripDestination', [dest_id, trip_id])
        connection.commit()
        return jsonify({'message': 'Destination removed successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to remove destination: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/deleteItem/<int:trip_id>/<int:item_id>', methods=['DELETE'])
def delete_item(trip_id, item_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteTripRequiredItem', [trip_id, item_id])
        connection.commit()
        return jsonify({'message': 'Item removed successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to remove item: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/deleteActivity/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteActivityById', [activity_id])
        connection.commit()
        return jsonify({'message': 'Activity deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete activity: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/deleteHomeStay/<int:accom_id>', methods=['DELETE'])
def delete_homestay(accom_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteHomeStayAccommodationById', [accom_id])
        connection.commit()
        return jsonify({'message': 'Homestay accommodation deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete homestay accommodation: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/deleteHotel/<int:accom_id>', methods=['DELETE'])
def delete_hotel(accom_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteHotelAccommodationById', [accom_id])
        connection.commit()
        return jsonify({'message': 'Hotel accommodation deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete hotel accommodation: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/deleteHostel/<int:accom_id>', methods=['DELETE'])
def delete_hostel(accom_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteHostelAccommodationById', [accom_id])
        connection.commit()
        return jsonify({'message': 'Hostel accommodation deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete hostel accommodation: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/updateTrip/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    data = request.json
    trip_name = data.get('trip_name')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    trip_status = data.get('trip_status')
    try:
        cursor = connection.cursor()
        cursor.callproc('UpdateTrip', (trip_id, trip_name, start_date, end_date, trip_status))
        connection.commit()
        return jsonify({'message': 'Trip updated successfully'}), 200
    except Error as e:
        print("Failed to update trip: ", str(e))
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/updateTraveller/<string:email_id>', methods=['PUT'])
def update_traveller(email_id):
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    unit_number = data.get('unit_number')
    street_name = data.get('street_name')
    street_number = data.get('street_number')
    city = data.get('city')
    state = data.get('state')
    zipcode = data.get('zipcode')

    try:
        cursor = connection.cursor()
        cursor.callproc('UpdateTraveller', (email_id, first_name, last_name, unit_number,
                                            street_name, street_number, city, state, zipcode))
        connection.commit()
        return jsonify({'message': 'Traveller updated successfully'}), 200
    except Error as e:
        print("Failed to update traveller: ", str(e))
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/updateDestination//<int:destination_id>', methods=['PUT'])
def update_destination(destination_id):
    data = request.json
    destination_name = data.get('destination_name')
    country = data.get('country')
    arrival_date = data.get('arrival_date')
    departure_date = data.get('departure_date')
    try:
        cursor = connection.cursor()
        cursor.callproc('UpdateDestination', (destination_id, destination_name, country, arrival_date, departure_date))
        connection.commit()
        return jsonify({'message': 'Destination updated successfully'}), 200
    except Error as e:
        print("Failed to update destination: ", str(e))
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()

@app.route('/allTrips', methods=['GET'])
def all_trips():
    cursor = connection.cursor()
    cursor.execute("""
        SELECT 
            t.trip_name AS 'Trip Name', 
            t.start_date AS 'Start Date', 
            t.end_date AS 'End Date', 
            t.trip_status AS 'Trip Status',
            d.destination_name AS 'Destination Name', 
            d.country AS 'Country', 
            d.arrival_date AS 'Arrival Date', 
            d.departure_date AS 'Departure Date',
            a.activity_location AS 'Activity Location', 
            a.activity_description AS 'Activity Description', 
            a.activity_date AS 'Activity Date',
            a.start_time AS 'Start Time', 
            a.end_time AS 'End Time', 
            a.cost AS 'Cost'
        FROM Trip t
        JOIN Trip_Has_Destination thd ON t.trip_id = thd.trip_id
        JOIN Destination d ON thd.destination_id = d.destination_id
        JOIN Activity a ON d.destination_id = a.destination_id;
    """)
    trips = cursor.fetchall()
    cursor.close()
    columns = [desc[0] for desc in cursor.description]
    trip_list = [dict(zip(columns, trip)) for trip in trips]
    return jsonify(trip_list)


@app.route('/getAccommodationChoices', methods=['GET'])
def get_accommodation_choices():
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.callproc('GetAccommodationChoicesByTravelDuration')
        results = cursor.fetchall()
        return jsonify({'accommodations': results}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/averageActivityCostByCountry', methods=['GET'])
def average_activity_cost_by_country():
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.callproc('GetAverageActivityCostByCountry')
        results = cursor.fetchall()
        return jsonify({'average_activity_costs': results}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/commonPackingItems', methods=['GET'])
def common_packing_items():
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.callproc('GetCommonPackingItems')
        results = cursor.fetchall()
        return jsonify({'common_packing_items': results}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/destinationPopularityOverTime', methods=['GET'])
def destination_popularity_over_time():
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.callproc('GetDestinationPopularityOverTime')
        results = cursor.fetchall()
        return jsonify({'destination_popularity': results}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/travelerTripCountsAndExpenses', methods=['GET'])
def traveler_trip_counts_and_expenses():
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.callproc('GetTravelerTripCountsAndExpenses')
        results = cursor.fetchall()
        return jsonify({'traveler_trips_and_expenses': results}), 200
    except Error as e:
        print(f"Database error: {e}")
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


if __name__ == '__main__':
    with open('configs.json', 'r') as file:
        configs = json.load(file)
    connection = connect_to_database(configs["db_username"], configs["db_password"])
    if connection is not None:
        app.run(debug=True, port=int(configs["port"]))
    else:
        print("Cant connect to db")
        exit(-1)
