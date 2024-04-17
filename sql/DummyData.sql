-- Dummy data for Traveller table
INSERT INTO traveller (email_id, mobile_number, first_name, last_name, gender, date_of_birth, unit_number, street_name,
                       street_number, city, state, zipcode)
VALUES ('example1@example.com', '1234567890', 'John', 'Doe', 'Male', '1990-01-01', 101, 'Main St', 123, 'City1',
        'State1', '12345'),
       ('example2@example.com', '9876543210', 'Jane', 'Doe', 'Female', '1992-03-15', 202, 'Broadway', 456, 'City2',
        'State2', '67890'),
       ('example3@example.com', '1112223333', 'Alice', 'Smith', 'Female', '1985-06-20', 303, 'Park Ave', 789, 'City3',
        'State3', '34567'),
       ('example4@example.com', '4445556666', 'Bob', 'Johnson', 'Male', '1978-11-10', 404, 'Oak St', 1011, 'City4',
        'State4', '89012'),
       ('example5@example.com', '7778889999', 'Emily', 'Brown', 'Female', '2000-09-25', 505, 'Cedar St', 1213, 'City5',
        'State5', '23456');

-- Dummy data for Trip table
INSERT INTO trip (trip_name, start_date, end_date, trip_status)
VALUES ('Trip 1', '2024-05-01', '2024-05-10', 'Planning In Progress'),
       ('Trip 2', '2024-06-15', '2024-06-25', 'Planned Successfully'),
       ('Trip 3', '2024-07-01', '2024-07-10', 'Ongoing'),
       ('Trip 4', '2024-08-15', '2024-08-25', 'Completed'),
       ('Trip 5', '2024-09-01', '2024-09-10', 'Planning In Progress');

-- Dummy data for Expense table
INSERT INTO expense (expense_date, expense_category, expense_description, amount, currency, trip_id)
VALUES ('2024-05-02', 'Food', 'Dinner at a restaurant', 50.00, 'USD', 1),
       ('2024-05-05', 'Transportation', 'Taxi fare', 20.00, 'USD', 1),
       ('2024-06-16', 'Sightseeing', 'Entrance fee to museum', 10.00, 'USD', 2),
       ('2024-07-02', 'Food', 'Lunch at a cafe', 30.00, 'USD', 3),
       ('2024-07-05', 'Shopping', 'Souvenirs', 40.00, 'USD', 3),
       ('2024-08-17', 'Transportation', 'Bus tickets', 15.00, 'USD', 4),
       ('2024-08-20', 'Food', 'Dinner at a local restaurant', 60.00, 'USD', 4),
       ('2024-09-02', 'Transportation', 'Subway fare', 5.00, 'USD', 5),
       ('2024-09-05', 'Food', 'Street food', 25.00, 'USD', 5);

-- Dummy data for Destination table
INSERT INTO destination (destination_name, country, arrival_date, departure_date)
VALUES ('Destination 1', 'Country1', '2024-05-01', '2024-05-10'),
       ('Destination 2', 'Country2', '2024-06-15', '2024-06-25'),
       ('Destination 3', 'Country3', '2024-07-01', '2024-07-10'),
       ('Destination 4', 'Country4', '2024-08-15', '2024-08-25'),
       ('Destination 5', 'Country5', '2024-09-01', '2024-09-10');

-- Dummy data for Activity table
INSERT INTO activity (activity_location, activity_description, activity_date, start_time, end_time, cost,
                      destination_id)
VALUES ('Activity 1', 'Description 1', '2024-05-02', '09:00:00', '12:00:00', 30.00, 1),
       ('Activity 2', 'Description 2', '2024-06-16', '10:00:00', '13:00:00', 20.00, 2),
       ('Activity 3', 'Description 3', '2024-07-02', '11:00:00', '14:00:00', 40.00, 3),
       ('Activity 4', 'Description 4', '2024-08-17', '12:00:00', '15:00:00', 25.00, 4),
       ('Activity 5', 'Description 5', '2024-09-02', '13:00:00', '16:00:00', 35.00, 5),
       ('Activity 6', 'Description 6', '2024-09-02', '13:00:00', '16:00:00', 35.00, 5);

-- Dummy data for Activity_SightSeeing table
INSERT INTO activity_sightSeeing (activity_id, site_type, site_description)
VALUES (1, 'Museum', 'Description of museum sightseeing'),
       (2, 'Historical Site', 'Description of historical site visit'),
       (5, 'Beach Visit', 'Description of beach visit');

-- Dummy data for Activity_AdventureSport table
INSERT INTO activity_adventuresport (activity_id, sport_type, minimum_age, other_restrictions)
VALUES (3, 'Hiking', 12, 'No other restrictions'),
       (4, 'Rock Climbing', 15, 'Experience required');

-- Dummy data for Accommodation_HomeStay table
INSERT INTO accommodation_homeStay (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date,
                                    street_name, street_number, city, state, zipcode, destination_id, number_of_rooms,
                                    is_cook_available, stay_type, is_pet_allowed)
VALUES ('HomeStay 1', 50.00, '1112223333', '2024-05-01', '2024-05-10', 'Main St', '456', 'City1', 'State1', '12345', 1,
        2, 1, 'Entire Home', 0),
       ('HomeStay 2', 60.00, '4445556666', '2024-06-15', '2024-06-25', 'Broadway', '789', 'City2', 'State2', '67890', 2,
        3, 0, 'Private Room', 1),
       ('HomeStay 3', 70.00, '7778889999', '2024-07-01', '2024-07-10', 'Park Ave', '1011', 'City3', 'State3', '34567',
        3, 1, 1, 'Shared Room', 0),
       ('HomeStay 4', 80.00, '9990001111', '2024-08-15', '2024-08-25', 'Oak St', '1213', 'City4', 'State4', '89012', 4,
        2, 0, 'Entire Home', 1),
       ('HomeStay 5', 90.00, '1231231234', '2024-09-01', '2024-09-10', 'Cedar St', '1415', 'City5', 'State5', '23456',
        5, 3, 1, 'Private Room', 0);

-- Dummy data for Accommodation_Hotel table
INSERT INTO accommodation_hotel (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date,
                                 street_name, street_number, city, state, zipcode, destination_id, number_of_rooms,
                                 complimentary_meal, star_rating)
VALUES ('Hotel 1', 100.00, '2223334444', '2024-05-01', '2024-05-10', 'Main St', '101', 'City1', 'State1', '12345', 1, 2,
        1, '3'),
       ('Hotel 2', 120.00, '5556667777', '2024-06-15', '2024-06-25', 'Broadway', '202', 'City2', 'State2', '67890', 2,
        3, 0, '4'),
       ('Hotel 3', 140.00, '8889990000', '2024-07-01', '2024-07-10', 'Park Ave', '303', 'City3', 'State3', '34567', 3,
        1, 1, '5'),
       ('Hotel 4', 160.00, '1112223333', '2024-08-15', '2024-08-25', 'Oak St', '404', 'City4', 'State4', '89012', 4, 2,
        0, '4'),
       ('Hotel 5', 180.00, '4445556666', '2024-09-01', '2024-09-10', 'Cedar St', '505', 'City5', 'State5', '23456', 5,
        3, 1, '3');

-- Dummy data for Accommodation_Hostel table
INSERT INTO accommodation_hostel (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date,
                                  street_name, street_number, city, state, zipcode, destination_id, meal_service,
                                  bathroom_type, free_wifi, mixed_gender_dorm)
VALUES ('Hostel 1', 20.00, '1231231234', '2024-05-01', '2024-05-10', 'Main St', '303', 'City1', 'State1', '12345', 1, 1,
        'Shared', 1, 1),
       ('Hostel 2', 25.00, '4564564567', '2024-06-15', '2024-06-25', 'Broadway', '404', 'City2', 'State2', '67890', 2,
        1, 'Private', 1, 0),
       ('Hostel 3', 30.00, '7897897890', '2024-07-01', '2024-07-10', 'Park Ave', '505', 'City3', 'State3', '34567', 3,
        1, 'Shared', 1, 1),
       ('Hostel 4', 35.00, '0120120123', '2024-08-15', '2024-08-25', 'Oak St', '606', 'City4', 'State4', '89012', 4, 1,
        'Private', 1, 0),
       ('Hostel 5', 40.00, '3453453456', '2024-09-01', '2024-09-10', 'Cedar St', '707', 'City5', 'State5', '23456', 5,
        1, 'Shared', 1, 1);

-- Dummy data for EssentialPackingItems table
INSERT INTO essential_packing_item (item_name)
VALUES ('Clothes'),
       ('Toothbrush'),
       ('Sunscreen'),
       ('Camera'),
       ('Medications'),
       ('Sunglasses'),
       ('Hat'),
       ('Swimsuit'),
       ('Book'),
       ('Charger');

-- Dummy data for Traveller_Plans_Trip table
INSERT INTO traveller_plans_trip (email_id, trip_id)
VALUES ('example1@example.com', 1),
       ('example2@example.com', 2),
       ('example3@example.com', 3),
       ('example4@example.com', 4),
       ('example5@example.com', 5);

-- Dummy data for Trip_Requires_Item table
INSERT INTO trip_requires_item (trip_id, item_id)
VALUES (1, 1),
       (1, 2),
       (2, 3),
       (2, 4),
       (3, 5),
       (3, 6),
       (4, 7),
       (4, 8),
       (5, 9),
       (5, 10);

-- Dummy data for Trip_Has_Destination table
INSERT INTO trip_has_destination (destination_id, trip_id, transportation_mode, travel_duration)
VALUES (1, 1, 'Flight', '03:00:00'),
       (2, 2, 'Train', '04:30:00'),
       (3, 3, 'Car', '05:00:00'),
       (4, 4, 'Bus', '06:00:00'),
       (5, 5, 'Boat', '07:00:00');
