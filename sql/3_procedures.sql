DROP PROCEDURE IF EXISTS add_traveller;
DROP PROCEDURE IF EXISTS add_trip;
DROP PROCEDURE IF EXISTS delete_trip_by_id;
DROP PROCEDURE IF EXISTS delete_activity_by_id;
DROP PROCEDURE IF EXISTS delete_homestay_accommodation_by_id;
DROP PROCEDURE IF EXISTS delete_hotel_accommodation_by_id;
DROP PROCEDURE IF EXISTS delete_hostel_accommodation_by_id;
DROP PROCEDURE IF EXISTS add_traveller_trip_plan;
DROP PROCEDURE IF EXISTS delete_trip_destination;
DROP PROCEDURE IF EXISTS add_expense;
DROP PROCEDURE IF EXISTS delete_expense_by_id;
DROP PROCEDURE IF EXISTS add_destination;
DROP PROCEDURE IF EXISTS add_activity;
DROP PROCEDURE IF EXISTS add_sightseeing_activity;
DROP PROCEDURE IF EXISTS add_adventuresport_activity;
DROP PROCEDURE IF EXISTS add_homestay_accommodation;
DROP PROCEDURE IF EXISTS add_hotel_accommodation;
DROP PROCEDURE IF EXISTS add_hostel_accommodation;
DROP PROCEDURE IF EXISTS add_essential_packing_item;
DROP PROCEDURE IF EXISTS delete_trip_required_item;
DROP PROCEDURE IF EXISTS add_trip_destination;
DROP PROCEDURE IF EXISTS add_trip_item;
DROP PROCEDURE IF EXISTS update_trip;
DROP PROCEDURE IF EXISTS update_traveller;
DROP PROCEDURE IF EXISTS update_destination;
DROP PROCEDURE IF EXISTS get_traveller_by_email;
DROP PROCEDURE IF EXISTS get_trips_by_traveller_email;
DROP PROCEDURE IF EXISTS get_traveler_trip_counts_and_expenses;
DROP PROCEDURE IF EXISTS get_destination_popularity_over_time;
DROP PROCEDURE IF EXISTS get_common_packing_items;
DROP PROCEDURE IF EXISTS get_average_activity_cost_by_country;
DROP PROCEDURE IF EXISTS get_accommodation_choices_by_travel_duration;
DROP PROCEDURE IF EXISTS update_trip_has_destination;

DELIMITER //

-- Procedure to add a new traveller
CREATE PROCEDURE add_traveller(
    IN email VARCHAR(255),
    IN mobile VARCHAR(20),
    IN fname VARCHAR(100),
    IN lname VARCHAR(100),
    IN gen VARCHAR(10),
    IN dob DATE,
    IN unit INT,
    IN street VARCHAR(255),
    IN street_no INT,
    IN city VARCHAR(100),
    IN state VARCHAR(100),
    IN zip VARCHAR(20)
)
BEGIN
    IF EXISTS (SELECT 1 FROM Traveller WHERE email_id = email) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'An account with this email already exists.';
    ELSE
        INSERT INTO traveller (email_id, mobile_number, first_name, last_name, gender, date_of_birth, unit_number,
        street_name, street_number, city, state, zipcode)
        VALUES (email, mobile, fname, lname, gen, dob, unit, street, street_no, city, state, zip);
    END IF;
END //

-- Procedure to add a new trip
CREATE PROCEDURE add_trip(
    IN trip_name VARCHAR(255),
    IN start_date DATE,
    IN end_date DATE,
    IN status ENUM('Planning In Progress','Planned Successfully','Ongoing', 'Completed')
)
BEGIN
    INSERT INTO trip (trip_name, start_date, end_date, trip_status)
    VALUES (trip_name, start_date, end_date, status);
END //

-- Procedure to delete a trip by trip ID
CREATE PROCEDURE delete_trip_by_id(IN id INT)
BEGIN
    DELETE FROM trip WHERE trip_id = id;
END //

-- Procedure to delete an activity by activity ID
CREATE PROCEDURE delete_activity_by_id(IN act_id INT)
BEGIN
    DELETE FROM activity_sightseeing WHERE activity_id = act_id;
    DELETE FROM activity_adventuresport WHERE activity_id = act_id;
    DELETE FROM activity WHERE activity_id = act_id;
END //

-- Procedure to delete a homestay accommodation by accommodation ID
CREATE PROCEDURE delete_homestay_accommodation_by_id(IN accom_id INT)
BEGIN
    DELETE FROM accommodation_homestay WHERE accommodation_id = accom_id;
END //

-- Procedure to delete a hotel accommodation by accommodation ID
CREATE PROCEDURE delete_hotel_accommodation_by_id(IN accom_id INT)
BEGIN
    DELETE FROM accommodation_hotel WHERE accommodation_id = accom_id;
END //

-- Procedure to delete a hostel accommodation by accommodation ID
CREATE PROCEDURE delete_hostel_accommodation_by_id(IN accom_id INT)
BEGIN
    DELETE FROM Accommodation_Hostel WHERE accommodation_id = accom_id;
END //

-- Procedure to add a traveller's trip plan
CREATE PROCEDURE add_traveller_trip_plan(
    IN email VARCHAR(255),
    IN trip_id INT
)
BEGIN
    INSERT INTO traveller_plans_trip (email_id, trip_id)
    VALUES (email, trip_id);
END //

-- Procedure to delete a trip's destination by destination ID and trip ID
CREATE PROCEDURE delete_trip_destination(
    IN dest_id INT,
    IN trip_id INT
)
BEGIN
    DELETE FROM Trip_Has_Destination WHERE destination_id = dest_id AND trip_id = trip_id;
END //

 -- Procedure to add a new expense
 CREATE PROCEDURE add_expense(
     IN exp_date DATE,
     IN exp_category VARCHAR(100),
     IN exp_description TEXT,
     IN amt DECIMAL(10, 2),
     IN curr VARCHAR(10),
     IN trip INT
 )
 BEGIN
     INSERT INTO expense (expense_date, expense_category, expense_description, amount, currency, trip_id)
     VALUES (exp_date, exp_category, exp_description, amt, curr, trip);
 END //

 -- Procedure to delete an expense by expense ID
 CREATE PROCEDURE delete_expense_by_id(IN exp_id INT)
 BEGIN
     DELETE FROM Expense WHERE expense_id = exp_id;
 END //

 -- Procedure to add a new destination
 CREATE PROCEDURE add_destination(
     IN dest_name VARCHAR(255),
     IN cntry VARCHAR(100),
     IN arr_date DATE,
     IN dep_date DATE
 )
 BEGIN
     INSERT INTO destination (destination_name, country, arrival_date, departure_date)
     VALUES (dest_name, cntry, arr_date, dep_date);
 END //

 -- Procedure to add a new activity
 CREATE PROCEDURE add_activity(
     IN loc VARCHAR(255),
     IN description TEXT,
     IN act_date DATE,
     IN start_time TIME,
     IN end_time TIME,
     IN cst DECIMAL(10, 2),
     IN dest_id INT
 )
 BEGIN
     INSERT INTO activity (activity_location, activity_description, activity_date, start_time, end_time, cost,
     destination_id)
     VALUES (loc, description, act_date, start_time, end_time, cst, dest_id);
 END //

 -- Procedure to add a new sightseeing activity
 CREATE PROCEDURE add_sightseeing_activity(
     IN act_id INT,
     IN site_type VARCHAR(50),
     IN site_description TEXT
 )
 BEGIN
     INSERT INTO activity_sightseeing (activity_id, site_type, site_description)
     VALUES (act_id, site_type, site_description);
 END //

 -- Procedure to add a new adventure sport activity
 CREATE PROCEDURE add_adventuresport_activity(
     IN act_id INT,
     IN sport_type VARCHAR(50),
     IN min_age INT,
     IN restrictions TEXT
 )
 BEGIN
     INSERT INTO activity_adventuresport (activity_id, sport_type, minimum_age, other_restrictions)
     VALUES (act_id, sport_type, min_age, restrictions);
 END //

-- Procedure to add a new homestay accommodation
 CREATE PROCEDURE add_homestay_accommodation(
     IN name VARCHAR(255),
     IN cost DECIMAL(10, 2),
     IN phone VARCHAR(20),
     IN checkin DATE,
     IN checkout DATE,
     IN street VARCHAR(255),
     IN street_no VARCHAR(255),
     IN city VARCHAR(255),
     IN state VARCHAR(255),
     IN zip VARCHAR(20),
     IN dest_id INT,
     IN rooms INT,
     IN cook_avail BOOLEAN,
     IN stay_type VARCHAR(255),
     IN pet_allowed BOOLEAN
 )
 BEGIN
     INSERT INTO accommodation_homeStay (accommodation_name, cost_per_night, telephone_number, checkin_date,
     checkout_date, street_name, street_number, city, state, zipcode, destination_id, number_of_rooms,
     is_cook_available, stay_type, is_pet_allowed)
     VALUES (name, cost, phone, checkin, checkout, street, street_no, city, state, zip, dest_id, rooms, cook_avail,
     stay_type, pet_allowed);
 END //

 -- Procedure to add a new hotel accommodation
 CREATE PROCEDURE add_hotel_accommodation(
     IN name VARCHAR(255),
     IN cost DECIMAL(10, 2),
     IN phone VARCHAR(20),
     IN checkin DATE,
     IN checkout DATE,
     IN street VARCHAR(255),
     IN street_no VARCHAR(255),
     IN city VARCHAR(255),
     IN state VARCHAR(255),
     IN zip VARCHAR(20),
     IN dest_id INT,
     IN rooms INT,
     IN meal BOOLEAN,
     IN star ENUM('1','2','3','4','5')
 )
 BEGIN
     INSERT INTO accommodation_hotel (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date,
     street_name, street_number, city, state, zipcode, destination_id, number_of_rooms, complimentary_meal, star_rating)
     VALUES (name, cost, phone, checkin, checkout, street, street_no, city, state, zip, dest_id, rooms, meal, star);
 END //

-- Procedure to add a new hostel accommodation
 CREATE PROCEDURE add_hostel_accommodation(
     IN name VARCHAR(255),
     IN cost DECIMAL(10, 2),
     IN phone VARCHAR(20),
     IN checkin DATE,
     IN checkout DATE,
     IN street VARCHAR(255),
     IN street_no VARCHAR(255),
     IN city VARCHAR(255),
     IN state VARCHAR(255),
     IN zip VARCHAR(20),
     IN dest_id INT,
     IN meal BOOLEAN,
     IN bath_type ENUM('Shared', 'Private'),
     IN wifi BOOLEAN,
     IN mixed_dorm BOOLEAN
 )
 BEGIN
     INSERT INTO accommodation_hostel (accommodation_name, cost_per_night, telephone_number, checkin_date,
     checkout_date, street_name, street_number, city, state, zipcode, destination_id, meal_service, bathroom_type,
     free_wifi, mixed_gender_dorm)
     VALUES (name, cost, phone, checkin, checkout, street, street_no, city, state, zip, dest_id, meal, bath_type, wifi,
     mixed_dorm);
 END //

 -- Procedure to add a new essential packing item
 CREATE PROCEDURE add_essential_packing_item(
     IN item_name VARCHAR(255)
 )
 BEGIN
     INSERT INTO essential_packing_item (item_name)
     VALUES (item_name);
 END //

 -- Procedure to delete a trip's required item by trip ID and item ID
 CREATE PROCEDURE delete_trip_required_item(
     IN p_trip_id INT,
     IN p_item_id INT
 )
 BEGIN
     DELETE FROM trip_requires_item WHERE trip_id = p_trip_id AND item_id = p_item_id;
 END //

 -- Procedure to add a trip's destination
 CREATE PROCEDURE add_trip_destination(
     IN dest_id INT,
     IN trip_id INT,
     IN transport_mode TEXT,
     IN travel_dur TIME
 )
 BEGIN
     INSERT INTO trip_has_destination (destination_id, trip_id, transportation_mode, travel_duration)
     VALUES (dest_id, trip_id, transport_mode, travel_dur);
 END //

 -- Procedure to update a trip has destination
 CREATE PROCEDURE update_trip_has_destination(
     IN p_dest_id INT,
     IN p_trip_id INT,
     IN p_transport_mode TEXT,
     IN p_travel_dur TIME
 )
 BEGIN
     UPDATE trip_has_destination
     SET transportation_mode = p_transport_mode,
     travel_duration = p_travel_dur
     WHERE
     trip_id = p_trip_id AND destination_id = p_dest_id;
 END //

 -- Procedure to add a trip's essential item
 CREATE PROCEDURE add_trip_item(
     IN trip_id INT,
     IN item_id INT
 )
 BEGIN
     INSERT INTO trip_requires_item (trip_id, item_id)
     VALUES (trip_id, item_id);
 END //

-- Procedure to update trip table
CREATE PROCEDURE update_trip(
    IN p_trip_id INT,
    IN p_trip_name VARCHAR(255),
    IN p_start_date DATE,
    IN p_end_date DATE,
    IN p_trip_status ENUM('Planning In Progress','Planned Successfully','Ongoing', 'Completed')
)
BEGIN
    UPDATE trip
    SET
        trip_name = p_trip_name,
        start_date = p_start_date,
        end_date = p_end_date,
        trip_status = p_trip_status
    WHERE
        trip_id = p_trip_id;
END//

-- Procedure to update traveller table
CREATE PROCEDURE update_traveller(IN p_email_id VARCHAR(255), IN p_first_name VARCHAR(100), IN p_last_name VARCHAR(100),
                                IN p_unit_number INT,
                                IN p_street_name VARCHAR(255), IN p_street_number INT, IN p_city VARCHAR(100),
                                IN p_state VARCHAR(100), IN p_zipcode VARCHAR(20))
BEGIN
    UPDATE traveller
    SET first_name = p_first_name,
        last_name = p_last_name,
        unit_number = p_unit_number,
        street_name = p_street_name,
        street_number = p_street_number,
        city = p_city,
        state = p_state,
        zipcode = p_zipcode
    WHERE email_id = p_email_id;
END //

-- Procedure to update destination table
CREATE PROCEDURE update_destination(
    IN p_destination_id INT,
    IN p_destination_name VARCHAR(255),
    IN p_country VARCHAR(100),
    IN p_arrival_date DATE,
    IN p_departure_date DATE
)
BEGIN
    UPDATE destination
    SET destination_name = p_destination_name,
        country = p_country,
        arrival_date = p_arrival_date,
        departure_date = p_departure_date
    WHERE destination_id = p_destination_id;
END //

-- Get traveller by email
CREATE PROCEDURE get_traveller_by_email(IN email VARCHAR(255))
BEGIN
    SELECT * FROM Traveller WHERE email_id = email;
END //

-- Get trips by traveller email
CREATE PROCEDURE get_trips_by_traveller_email(IN email_id VARCHAR(255))
BEGIN
    select * from trip where trip_id in (select trip_id from traveller_plans_trip where
    traveller_plans_trip.email_id=email_id);
END//


CREATE PROCEDURE get_traveler_trip_counts_and_expenses()
BEGIN
    SELECT traveller.email_id, traveller.first_name, traveller.last_name,
           COUNT(DISTINCT trip.trip_id) AS total_trips,
           SUM(Expense.amount) AS total_expenses
    FROM traveller
    JOIN traveller_plans_trip ON traveller.email_id = traveller_plans_trip.email_id
    JOIN Trip ON traveller_plans_trip.trip_id = trip.trip_id
    LEFT JOIN expense ON trip.trip_id = expense.trip_id
    GROUP BY traveller.email_id;
END //


CREATE PROCEDURE get_destination_popularity_over_time()
BEGIN
    SELECT destination.destination_name, YEAR(trip.start_date) AS year, MONTH(trip.start_date) AS month,
           COUNT(*) AS visit_count
    FROM destination
    JOIN trip_has_destination ON destination.destination_id = trip_has_destination.destination_id
    JOIN trip ON trip_has_destination.trip_id = trip.trip_id
    WHERE trip.trip_status = 'Completed'
    GROUP BY destination.destination_name, YEAR(trip.start_date), MONTH(trip.start_date)
    ORDER BY destination.destination_name, year, month;
END //


CREATE PROCEDURE get_common_packing_items()
BEGIN
    SELECT essential_packing_item.item_name, COUNT(*) AS item_count
    FROM essential_packing_item
    JOIN Trip_Requires_Item ON essential_packing_item.item_id = Trip_Requires_Item.item_id
    GROUP BY essential_packing_item.item_name
    ORDER BY item_count DESC
    LIMIT 10;
END //


CREATE PROCEDURE get_average_activity_cost_by_country()
BEGIN
    SELECT Destination.country, AVG(Activity.cost) AS average_cost
    FROM Activity
    JOIN Destination ON Activity.destination_id = Destination.destination_id
    GROUP BY Destination.country;
END //


CREATE PROCEDURE get_accommodation_choices_by_travel_duration()
BEGIN
    SELECT
        Accommodation_Hotel.accommodation_name,
        DATEDIFF(Accommodation_Hotel.checkout_date, Accommodation_Hotel.checkin_date) AS duration,
        COUNT(*) AS booking_count
    FROM Accommodation_Hotel
    GROUP BY Accommodation_Hotel.accommodation_name, duration
    ORDER BY duration DESC, booking_count DESC;
END //


DELIMITER ;
