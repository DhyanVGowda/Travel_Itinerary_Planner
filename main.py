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


@app.route('/deleteTraveller/<email>', methods=['DELETE'])
def delete_traveller(email):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteTravellerByEmail', [email])
        connection.commit()
        return jsonify({'message': 'Traveller deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete traveller: ' + str(e)}), 500
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


@app.route('/deleteDestination/<int:dest_id>', methods=['DELETE'])
def delete_destination(dest_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteDestinationById', [dest_id])
        connection.commit()
        return jsonify({'message': 'Destination deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete destination: ' + str(e)}), 500
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


@app.route('/deleteExpense/<int:exp_id>', methods=['DELETE'])
def delete_expense(exp_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteExpenseById', [exp_id])
        connection.commit()
        return jsonify({'message': 'Expense deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete expense: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/deleteSightSeeingActivity/<int:act_id>', methods=['DELETE'])
def delete_sightseeing_activity(act_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteSightseeingActivityById', [act_id])
        connection.commit()
        return jsonify({'message': 'Sightseeing activity deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete sightseeing activity: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/deleteAdventureSportActivity/<int:act_id>', methods=['DELETE'])
def delete_adventure_sport_activity(act_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteAdventureSportActivityById', [act_id])
        connection.commit()
        return jsonify({'message': 'Adventure sport activity deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete adventure sport activity: ' + str(e)}), 500
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


@app.route('/deleteEssentialPackingItems/<int:item_id>', methods=['DELETE'])
def delete_packing_item(item_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteEssentialPackingItemById', [item_id])
        connection.commit()
        return jsonify({'message': 'Packing item deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete packing item: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/deleteTripRequiresItem/<int:trip_id>/<int:item_id>', methods=['DELETE'])
def delete_trip_required_item(trip_id, item_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteTripRequiredItem', [trip_id, item_id])
        connection.commit()
        return jsonify({'message': 'Trip required item deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete trip required item: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/deleteTravellerPlansTrip/<email>/<int:trip_id>', methods=['DELETE'])
def delete_traveller_trip_plan(email, trip_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('DeleteTravellerTripPlan', [email, trip_id])
        connection.commit()
        return jsonify({'message': 'Traveller trip plan deleted successfully'}), 200
    except Error as e:
        connection.rollback()
        return jsonify({'error': 'Failed to delete traveller trip plan: ' + str(e)}), 500
    finally:
        cursor.close()


@app.route('/getExpenseById/<int:exp_id>', methods=['GET'])
def get_expense_by_id(exp_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetExpenseById', [exp_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getDestinationById/<int:dest_id>', methods=['GET'])
def get_destination_by_id(dest_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetDestinationById', [dest_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getActivityById/<int:act_id>', methods=['GET'])
def get_activity_by_id(act_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetActivityById', [act_id])
        results = cursor.fetchall()
        response_json = json.dumps(results, cls=CustomEncoder)
        return Response(response_json), 200
    except Error as e:
        return Response(json.dumps({'error': str(e)})), 500
    finally:
        cursor.close()


@app.route('/getSightSeeingActivityById/<int:act_id>', methods=['GET'])
def get_sightseeing_activity_by_id(act_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetSightSeeingActivityById', [act_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getAdventureSportActivityById/<int:act_id>', methods=['GET'])
def get_adventure_sport_activity_by_id(act_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetAdventureSportActivityById', [act_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getHomeStayAccomodationById/<int:accom_id>', methods=['GET'])
def get_homestay_accommodation_by_id(accom_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetHomeStayAccommodationById', [accom_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getAccommodationHotelById/<int:accom_id>', methods=['GET'])
def get_hotel_accommodation_by_id(accom_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetHotelAccommodationById', [accom_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getAccommodationHostelById/<int:accom_id>', methods=['GET'])
def get_hostel_accommodation_by_id(accom_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetHostelAccommodationById', [accom_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getEssentialPackingItemsById/<int:item_id>', methods=['GET'])
def get_essential_packing_item_by_id(item_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetEssentialPackingItemById', [item_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getTravellerPlansTripById/<email>/<int:trip_id>', methods=['GET'])
def get_traveller_trip_plan(email, trip_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetTravellerTripPlan', [email, trip_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getTripRequiresItem/<int:trip_id>/<int:item_id>', methods=['GET'])
def get_trip_required_item(trip_id, item_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetTripRequiredItem', [trip_id, item_id])
        results = cursor.fetchall()
        return jsonify(results), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/getTripHasDestination/<int:dest_id>/<int:trip_id>', methods=['GET'])
def get_trip_destination(dest_id, trip_id):
    try:
        cursor = connection.cursor()
        cursor.callproc('GetTripDestination', [dest_id, trip_id])
        results = cursor.fetchall()
        response_json = json.dumps(results, cls=CustomEncoder)
        return Response(response_json), 200
    except Error as e:
        error_message = json.dumps({'error': str(e)}, cls=CustomEncoder)
        return Response(error_message), 500
    finally:
        cursor.close()


@app.route('/addDestination', methods=['POST'])
def add_destination():
    data = request.get_json()
    try:
        cursor = connection.cursor()
        cursor.callproc('AddDestination', [
            data['destination_name'],
            data['country'],
            data['arrival_date'],
            data['departure_date']
        ])
        connection.commit()
        return jsonify({'message': 'Destination added successfully'}), 201
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addAccommodationHotel', methods=['POST'])
def add_hotel():
    data = request.get_json()
    try:
        cursor = connection.cursor()
        cursor.callproc('AddHotelAccommodation', [
            data['name'],
            data['cost_per_night'],
            data['telephone_number'],
            data['checkin_date'],
            data['checkout_date'],
            data['street_name'],
            data['street_number'],
            data['city'],
            data['state'],
            data['zipcode'],
            data['destination_id'],
            data['number_of_rooms'],
            data['complimentary_meal'],
            data['star_rating']
        ])
        connection.commit()
        return jsonify({'message': 'Hotel added successfully'}), 201
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addAccommodationHomeStay', methods=['POST'])
def add_homestay():
    data = request.get_json()
    try:
        cursor = connection.cursor()
        cursor.callproc('AddHomeStayAccommodation', [
            data['accommodation_name'],
            data['cost_per_night'],
            data['telephone_number'],
            data['checkin_date'],
            data['checkout_date'],
            data['street_name'],
            data['street_number'],
            data['city'],
            data['state'],
            data['zipcode'],
            data['destination_id'],
            data['number_of_rooms'],
            data.get('is_cook_available', False),
            data['stay_type'],
            data.get('is_pet_allowed', False)
        ])
        connection.commit()
        return jsonify({'message': 'Homestay added successfully'}), 201
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addAccommodationHostel', methods=['POST'])
def add_hostel():
    data = request.get_json()
    try:
        cursor = connection.cursor()
        cursor.callproc('AddHostelAccommodation', [
            data['accommodation_name'],
            data['cost_per_night'],
            data['telephone_number'],
            data['checkin_date'],
            data['checkout_date'],
            data['street_name'],
            data['street_number'],
            data['city'],
            data['state'],
            data['zipcode'],
            data['destination_id'],
            data.get('meal_service', False),
            data['bathroom_type'],
            data.get('free_wifi', False),
            data.get('mixed_gender_dorm', False)
        ])
        connection.commit()
        return jsonify({'message': 'Hostel added successfully'}), 201
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/activity', methods=['POST'])
def add_activity():
    data = request.get_json()
    try:
        cursor = connection.cursor()
        cursor.callproc('AddActivity', [
            data['activity_location'],
            data['activity_description'],
            data['activity_date'],
            data['start_time'],
            data['end_time'],
            data['cost'],
            data['destination_id']
        ])
        connection.commit()
        return jsonify({'message': 'Activity added successfully'}), 201
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addActivitySightSeeing', methods=['POST'])
def add_sightseeing():
    data = request.get_json()
    try:
        cursor = connection.cursor()
        cursor.callproc('AddSightseeingActivity', [
            data['activity_id'],
            data['site_type'],
            data['site_description']
        ])
        connection.commit()
        return jsonify({'message': 'Sightseeing activity added successfully'}), 201
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


@app.route('/addActivityAdventureSport', methods=['POST'])
def add_adventure_sport():
    data = request.get_json()
    try:
        cursor = connection.cursor()
        cursor.callproc('AddAdventureSportActivity', [
            data['activity_id'],
            data['sport_type'],
            data['minimum_age'],
            data['other_restrictions']
        ])
        connection.commit()
        return jsonify({'message': 'Adventure sport activity added successfully'}), 201
    except pymysql.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()


if __name__ == '__main__':
    username = "root"
    password = "Anvitha@2024"
    connection = connect_to_database(username, password)
    if connection is not None:
        app.run(debug=True)
    else:
        print("Cant connect to db")
        exit(-1)
