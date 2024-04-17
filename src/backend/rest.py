#
# @app.route('/deleteTraveller/<email>', methods=['DELETE'])
# def delete_traveller(email):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('DeleteTravellerByEmail', [email])
#         connection.commit()
#         return jsonify({'message': 'Traveller deleted successfully'}), 200
#     except Error as e:
#         connection.rollback()
#         return jsonify({'error': 'Failed to delete traveller: ' + str(e)}), 500
#     finally:
#         cursor.close()

# @app.route('/deleteExpense/<int:exp_id>', methods=['DELETE'])
# def delete_expense(exp_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('DeleteExpenseById', [exp_id])
#         connection.commit()
#         return jsonify({'message': 'Expense deleted successfully'}), 200
#     except Error as e:
#         connection.rollback()
#         return jsonify({'error': 'Failed to delete expense: ' + str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/deleteSightSeeingActivity/<int:act_id>', methods=['DELETE'])
# def delete_sightseeing_activity(act_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('DeleteSightseeingActivityById', [act_id])
#         connection.commit()
#         return jsonify({'message': 'Sightseeing activity deleted successfully'}), 200
#     except Error as e:
#         connection.rollback()
#         return jsonify({'error': 'Failed to delete sightseeing activity: ' + str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/deleteAdventureSportActivity/<int:act_id>', methods=['DELETE'])
# def delete_adventure_sport_activity(act_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('DeleteAdventureSportActivityById', [act_id])
#         connection.commit()
#         return jsonify({'message': 'Adventure sport activity deleted successfully'}), 200
#     except Error as e:
#         connection.rollback()
#         return jsonify({'error': 'Failed to delete adventure sport activity: ' + str(e)}), 500
#     finally:
#         cursor.close()
#
#
#
# @app.route('/deleteEssentialPackingItems/<int:item_id>', methods=['DELETE'])
# def delete_packing_item(item_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('DeleteEssentialPackingItemById', [item_id])
#         connection.commit()
#         return jsonify({'message': 'Packing item deleted successfully'}), 200
#     except Error as e:
#         connection.rollback()
#         return jsonify({'error': 'Failed to delete packing item: ' + str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/deleteTripRequiresItem/<int:trip_id>/<int:item_id>', methods=['DELETE'])
# def delete_trip_required_item(trip_id, item_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('DeleteTripRequiredItem', [trip_id, item_id])
#         connection.commit()
#         return jsonify({'message': 'Trip required item deleted successfully'}), 200
#     except Error as e:
#         connection.rollback()
#         return jsonify({'error': 'Failed to delete trip required item: ' + str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/deleteTravellerPlansTrip/<email>/<int:trip_id>', methods=['DELETE'])
# def delete_traveller_trip_plan(email, trip_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('DeleteTravellerTripPlan', [email, trip_id])
#         connection.commit()
#         return jsonify({'message': 'Traveller trip plan deleted successfully'}), 200
#     except Error as e:
#         connection.rollback()
#         return jsonify({'error': 'Failed to delete traveller trip plan: ' + str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getExpenseById/<int:exp_id>', methods=['GET'])
# def get_expense_by_id(exp_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetExpenseById', [exp_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getDestinationById/<int:dest_id>', methods=['GET'])
# def get_destination_by_id(dest_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetDestinationById', [dest_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getActivityById/<int:act_id>', methods=['GET'])
# def get_activity_by_id(act_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetActivityById', [act_id])
#         results = cursor.fetchall()
#         response_json = json.dumps(results, cls=CustomEncoder)
#         return Response(response_json), 200
#     except Error as e:
#         return Response(json.dumps({'error': str(e)})), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getSightSeeingActivityById/<int:act_id>', methods=['GET'])
# def get_sightseeing_activity_by_id(act_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetSightSeeingActivityById', [act_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getAdventureSportActivityById/<int:act_id>', methods=['GET'])
# def get_adventure_sport_activity_by_id(act_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetAdventureSportActivityById', [act_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getHomeStayAccomodationById/<int:accom_id>', methods=['GET'])
# def get_homestay_accommodation_by_id(accom_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetHomeStayAccommodationById', [accom_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getAccommodationHotelById/<int:accom_id>', methods=['GET'])
# def get_hotel_accommodation_by_id(accom_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetHotelAccommodationById', [accom_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getAccommodationHostelById/<int:accom_id>', methods=['GET'])
# def get_hostel_accommodation_by_id(accom_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetHostelAccommodationById', [accom_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getEssentialPackingItemsById/<int:item_id>', methods=['GET'])
# def get_essential_packing_item_by_id(item_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetEssentialPackingItemById', [item_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getTravellerPlansTripById/<email>/<int:trip_id>', methods=['GET'])
# def get_traveller_trip_plan(email, trip_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetTravellerTripPlan', [email, trip_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getTripRequiresItem/<int:trip_id>/<int:item_id>', methods=['GET'])
# def get_trip_required_item(trip_id, item_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetTripRequiredItem', [trip_id, item_id])
#         results = cursor.fetchall()
#         return jsonify(results), 200
#     except Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/getTripHasDestination/<int:dest_id>/<int:trip_id>', methods=['GET'])
# def get_trip_destination(dest_id, trip_id):
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('GetTripDestination', [dest_id, trip_id])
#         results = cursor.fetchall()
#         response_json = json.dumps(results, cls=CustomEncoder)
#         return Response(response_json), 200
#     except Error as e:
#         error_message = json.dumps({'error': str(e)}, cls=CustomEncoder)
#         return Response(error_message), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/addDestination', methods=['POST'])
# def add_destination():
#     data = request.get_json()
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('AddDestination', [
#             data['destination_name'],
#             data['country'],
#             data['arrival_date'],
#             data['departure_date']
#         ])
#         connection.commit()
#         return jsonify({'message': 'Destination added successfully'}), 201
#     except pymysql.Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/addAccommodationHotel', methods=['POST'])
# def add_hotel():
#     data = request.get_json()
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('AddHotelAccommodation', [
#             data['name'],
#             data['cost_per_night'],
#             data['telephone_number'],
#             data['checkin_date'],
#             data['checkout_date'],
#             data['street_name'],
#             data['street_number'],
#             data['city'],
#             data['state'],
#             data['zipcode'],
#             data['destination_id'],
#             data['number_of_rooms'],
#             data['complimentary_meal'],
#             data['star_rating']
#         ])
#         connection.commit()
#         return jsonify({'message': 'Hotel added successfully'}), 201
#     except pymysql.Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/addAccommodationHomeStay', methods=['POST'])
# def add_homestay():
#     data = request.get_json()
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('AddHomeStayAccommodation', [
#             data['accommodation_name'],
#             data['cost_per_night'],
#             data['telephone_number'],
#             data['checkin_date'],
#             data['checkout_date'],
#             data['street_name'],
#             data['street_number'],
#             data['city'],
#             data['state'],
#             data['zipcode'],
#             data['destination_id'],
#             data['number_of_rooms'],
#             data.get('is_cook_available', False),
#             data['stay_type'],
#             data.get('is_pet_allowed', False)
#         ])
#         connection.commit()
#         return jsonify({'message': 'Homestay added successfully'}), 201
#     except pymysql.Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/addAccommodationHostel', methods=['POST'])
# def add_hostel():
#     data = request.get_json()
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('AddHostelAccommodation', [
#             data['accommodation_name'],
#             data['cost_per_night'],
#             data['telephone_number'],
#             data['checkin_date'],
#             data['checkout_date'],
#             data['street_name'],
#             data['street_number'],
#             data['city'],
#             data['state'],
#             data['zipcode'],
#             data['destination_id'],
#             data.get('meal_service', False),
#             data['bathroom_type'],
#             data.get('free_wifi', False),
#             data.get('mixed_gender_dorm', False)
#         ])
#         connection.commit()
#         return jsonify({'message': 'Hostel added successfully'}), 201
#     except pymysql.Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/activity', methods=['POST'])
# def add_activity():
#     data = request.get_json()
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('AddActivity', [
#             data['activity_location'],
#             data['activity_description'],
#             data['activity_date'],
#             data['start_time'],
#             data['end_time'],
#             data['cost'],
#             data['destination_id']
#         ])
#         connection.commit()
#         return jsonify({'message': 'Activity added successfully'}), 201
#     except pymysql.Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/addActivitySightSeeing', methods=['POST'])
# def add_sightseeing():
#     data = request.get_json()
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('AddSightseeingActivity', [
#             data['activity_id'],
#             data['site_type'],
#             data['site_description']
#         ])
#         connection.commit()
#         return jsonify({'message': 'Sightseeing activity added successfully'}), 201
#     except pymysql.Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
#
#
# @app.route('/addActivityAdventureSport', methods=['POST'])
# def add_adventure_sport():
#     data = request.get_json()
#     try:
#         cursor = connection.cursor()
#         cursor.callproc('AddAdventureSportActivity', [
#             data['activity_id'],
#             data['sport_type'],
#             data['minimum_age'],
#             data['other_restrictions']
#         ])
#         connection.commit()
#         return jsonify({'message': 'Adventure sport activity added successfully'}), 201
#     except pymysql.Error as e:
#         return jsonify({'error': str(e)}), 500
#     finally:
#         cursor.close()
