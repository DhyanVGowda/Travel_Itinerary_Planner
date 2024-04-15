-- Procedure to add a new traveller
DELIMITER //
CREATE PROCEDURE AddTraveller(
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
        INSERT INTO Traveller (email_id, mobile_number, first_name, last_name, gender, date_of_birth, unit_number, street_name, street_number, city, state, zipcode)
        VALUES (email, mobile, fname, lname, gen, dob, unit, street, street_no, city, state, zip);
    END IF;
END //

-- Procedure to add a new trip
DELIMITER //
CREATE PROCEDURE AddTrip(
    IN trip_name VARCHAR(255),
    IN start_date DATE,
    IN end_date DATE,
    IN status ENUM('Planning In Progress','Planned Successfully','Ongoing', 'Completed')
)
BEGIN
    INSERT INTO Trip (trip_name, start_date, end_date, trip_status)
    VALUES (trip_name, start_date, end_date, status);
END //
DELIMITER ;

-- Procedure to delete a trip by trip ID
DELIMITER //
CREATE PROCEDURE DeleteTripById(IN id INT)
BEGIN
    DELETE FROM Trip WHERE trip_id = id;
END //
DELIMITER ;

-- Procedure to delete an activity by activity ID
DELIMITER //
CREATE PROCEDURE DeleteActivityById(IN act_id INT)
BEGIN
    DELETE FROM Activity_SightSeeing WHERE activity_id = act_id;
    DELETE FROM Activity_AdventureSport WHERE activity_id = act_id;
    DELETE FROM Activity WHERE activity_id = act_id;
END //
DELIMITER ;

-- Procedure to delete a homestay accommodation by accommodation ID
DELIMITER //
CREATE PROCEDURE DeleteHomeStayAccommodationById(IN accom_id INT)
BEGIN
    DELETE FROM Accommodation_HomeStay WHERE accommodation_id = accom_id;
END //
DELIMITER ;

-- Procedure to delete a hotel accommodation by accommodation ID
DELIMITER //
CREATE PROCEDURE DeleteHotelAccommodationById(IN accom_id INT)
BEGIN
    DELETE FROM Accommodation_Hotel WHERE accommodation_id = accom_id;
END //
DELIMITER ;

-- Procedure to delete a hostel accommodation by accommodation ID
DELIMITER //
CREATE PROCEDURE DeleteHostelAccommodationById(IN accom_id INT)
BEGIN
    DELETE FROM Accommodation_Hostel WHERE accommodation_id = accom_id;
END //
DELIMITER ;

-- Procedure to add a traveller's trip plan
DELIMITER //
CREATE PROCEDURE AddTravellerTripPlan(
    IN email VARCHAR(255),
    IN trip_id INT
)
BEGIN
    INSERT INTO Traveller_Plans_Trip (email_id, trip_id)
    VALUES (email, trip_id);
END //
DELIMITER ;

-- Procedure to delete a trip's destination by destination ID and trip ID
DELIMITER //
CREATE PROCEDURE DeleteTripDestination(
    IN dest_id INT,
    IN trip_id INT
)
BEGIN
    DELETE FROM Trip_Has_Destination WHERE destination_id = dest_id AND trip_id = trip_id;
END //
DELIMITER ;

-- Procedure to delete a traveller by email
-- DELIMITER //
-- CREATE PROCEDURE DeleteTravellerByEmail(IN email VARCHAR(255))
-- BEGIN
--     DELETE FROM Traveller WHERE email_id = email;
-- END //
-- DELIMITER ;

 -- Procedure to add a new expense
 DELIMITER //
 CREATE PROCEDURE AddExpense(
     IN exp_date DATE,
     IN exp_category VARCHAR(100),
     IN exp_description TEXT,
     IN amt DECIMAL(10, 2),
     IN curr VARCHAR(10),
     IN trip INT
 )
 BEGIN
     INSERT INTO Expense (expense_date, expense_category, expense_description, amount, currency, trip_id)
     VALUES (exp_date, exp_category, exp_description, amt, curr, trip);
 END //
 DELIMITER ;

 -- Procedure to delete an expense by expense ID
 DELIMITER //
 CREATE PROCEDURE DeleteExpenseById(IN exp_id INT)
 BEGIN
     DELETE FROM Expense WHERE expense_id = exp_id;
 END //
 DELIMITER ;



 -- Procedure to add a new destination
 DELIMITER //
 CREATE PROCEDURE AddDestination(
     IN dest_name VARCHAR(255),
     IN cntry VARCHAR(100),
     IN arr_date DATE,
     IN dep_date DATE
 )
 BEGIN
     INSERT INTO Destination (destination_name, country, arrival_date, departure_date)
     VALUES (dest_name, cntry, arr_date, dep_date);
 END //
 DELIMITER ;

-- -- Procedure to delete a destination by destination ID
-- DELIMITER //
-- CREATE PROCEDURE DeleteDestinationById(IN dest_id INT)
-- BEGIN
--     DELETE FROM Destination WHERE destination_id = dest_id;
-- END //
-- DELIMITER ;


 -- Procedure to add a new activity
 DELIMITER //
 CREATE PROCEDURE AddActivity(
     IN loc VARCHAR(255),
     IN description TEXT,
     IN act_date DATE,
     IN start_time TIME,
     IN end_time TIME,
     IN cst DECIMAL(10, 2),
     IN dest_id INT
 )
 BEGIN
     INSERT INTO Activity (activity_location, activity_description, activity_date, start_time, end_time, cost, destination_id)
     VALUES (loc, description, act_date, start_time, end_time, cst, dest_id);
 END //
 DELIMITER ;

 -- Procedure to add a new sightseeing activity
 DELIMITER //
 CREATE PROCEDURE AddSightseeingActivity(
     IN act_id INT,
     IN site_type VARCHAR(50),
     IN site_description TEXT
 )
 BEGIN
     INSERT INTO Activity_SightSeeing (activity_id, site_type, site_description)
     VALUES (act_id, site_type, site_description);
 END //
 DELIMITER ;

 -- Procedure to add a new adventure sport activity
 DELIMITER //
 CREATE PROCEDURE AddAdventureSportActivity(
     IN act_id INT,
     IN sport_type VARCHAR(50),
     IN min_age INT,
     IN restrictions TEXT
 )
 BEGIN
     INSERT INTO Activity_AdventureSport (activity_id, sport_type, minimum_age, other_restrictions)
     VALUES (act_id, sport_type, min_age, restrictions);
 END //
 DELIMITER ;

-- -- Procedure to add a new homestay accommodation
 DELIMITER //
 CREATE PROCEDURE AddHomeStayAccommodation(
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
     INSERT INTO Accommodation_HomeStay (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date, street_name, street_number, city, state, zipcode, destination_id, number_of_rooms, is_cook_available, stay_type, is_pet_allowed)
     VALUES (name, cost, phone, checkin, checkout, street, street_no, city, state, zip, dest_id, rooms, cook_avail, stay_type, pet_allowed);
 END //
 DELIMITER ;

 -- Procedure to add a new hotel accommodation
 DELIMITER //
 CREATE PROCEDURE AddHotelAccommodation(
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
     INSERT INTO Accommodation_Hotel (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date, street_name, street_number, city, state, zipcode, destination_id, number_of_rooms, complimentary_meal, star_rating)
     VALUES (name, cost, phone, checkin, checkout, street, street_no, city, state, zip, dest_id, rooms, meal, star);
 END //
-- DELIMITER ;

-- -- Procedure to add a new hostel accommodation
 DELIMITER //
 CREATE PROCEDURE AddHostelAccommodation(
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
     INSERT INTO Accommodation_Hostel (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date, street_name, street_number, city, state, zipcode, destination_id, meal_service, bathroom_type, free_wifi, mixed_gender_dorm)
     VALUES (name, cost, phone, checkin, checkout, street, street_no, city, state, zip, dest_id, meal, bath_type, wifi, mixed_dorm);
 END //
 DELIMITER ;

-- -- Procedure to add a new essential packing item
-- DELIMITER //
-- CREATE PROCEDURE AddEssentialPackingItem(
--     IN item_name VARCHAR(255)
-- )
-- BEGIN
--     INSERT INTO EssentialPackingItems (item_name)
--     VALUES (item_name);
-- END //
-- DELIMITER ;

-- -- Procedure to delete an essential packing item by item ID
-- DELIMITER //
-- CREATE PROCEDURE DeleteEssentialPackingItemById(IN item_id INT)
-- BEGIN
--     DELETE FROM EssentialPackingItems WHERE item_id = item_id;
-- END //
-- DELIMITER ;

-- -- Procedure to delete a traveller's trip plan by email and trip ID
-- DELIMITER //
-- CREATE PROCEDURE DeleteTravellerTripPlan(
--     IN email VARCHAR(255),
--     IN trip_id INT
-- )
-- BEGIN
--     DELETE FROM Traveller_Plans_Trip WHERE email_id = email AND trip_id = trip_id;
-- END //
-- DELIMITER ;



-- -- Procedure to add a trip's required item
-- DELIMITER //
-- CREATE PROCEDURE AddTripRequiredItem(
--     IN trip_id INT,
--     IN item_id INT
-- )
-- BEGIN
--     INSERT INTO Trip_Requires_Item (trip_id, item_id)
--     VALUES (trip_id, item_id);
-- END //
-- DELIMITER ;

-- -- Procedure to delete a trip's required item by trip ID and item ID
-- DELIMITER //
-- CREATE PROCEDURE DeleteTripRequiredItem(
--     IN trip_id INT,
--     IN item_id INT
-- )
-- BEGIN
--     DELETE FROM Trip_Requires_Item WHERE trip_id = trip_id AND item_id = item_id;
-- END //
-- DELIMITER ;

-- -- Procedure to add a trip's destination
-- DELIMITER //
-- CREATE PROCEDURE AddTripDestination(
--     IN dest_id INT,
--     IN trip_id INT,
--     IN transport_mode TEXT,
--     IN travel_dur TIME
-- )
-- BEGIN
--     INSERT INTO Trip_Has_Destination (destination_id, trip_id, transportation_mode, travel_duration)
--     VALUES (dest_id, trip_id, transport_mode, travel_dur);
-- END //
-- DELIMITER ;
