DELIMITER //

-- Traveller
CREATE PROCEDURE GetTravellerByEmail(IN email VARCHAR(255))
BEGIN
    SELECT * FROM Traveller WHERE email_id = email;
END //

-- Trip
CREATE PROCEDURE GetTripById(IN id INT)
BEGIN
    SELECT * FROM Trip WHERE trip_id = id;
END //

-- Expense
CREATE PROCEDURE GetExpenseById(IN exp_id INT)
BEGIN
    SELECT * FROM Expense WHERE expense_id = exp_id;
END //

-- Destination
CREATE PROCEDURE GetDestinationById(IN dest_id INT)
BEGIN
    SELECT * FROM Destination WHERE destination_id = dest_id;
END //

-- Activity
CREATE PROCEDURE GetActivityById(IN act_id INT)
BEGIN
    SELECT * FROM Activity WHERE activity_id = act_id;
END //

-- Activity SightSeeing
CREATE PROCEDURE GetSightSeeingActivityById(IN act_id INT)
BEGIN
    SELECT * FROM Activity_SightSeeing WHERE activity_id = act_id;
END //

-- Activity AdventureSport
CREATE PROCEDURE GetAdventureSportActivityById(IN act_id INT)
BEGIN
    SELECT * FROM Activity_AdventureSport WHERE activity_id = act_id;
END //

-- Accommodation HomeStay
CREATE PROCEDURE GetHomeStayAccommodationById(IN accom_id INT)
BEGIN
    SELECT * FROM Accommodation_HomeStay WHERE accommodation_id = accom_id;
END //

-- Accommodation Hotel
CREATE PROCEDURE GetHotelAccommodationById(IN accom_id INT)
BEGIN
    SELECT * FROM Accommodation_Hotel WHERE accommodation_id = accom_id;
END //

-- Accommodation Hostel
CREATE PROCEDURE GetHostelAccommodationById(IN accom_id INT)
BEGIN
    SELECT * FROM Accommodation_Hostel WHERE accommodation_id = accom_id;
END //

-- Essential Packing Items
CREATE PROCEDURE GetEssentialPackingItemById(IN item_id INT)
BEGIN
    SELECT * FROM EssentialPackingItems WHERE item_id = item_id;
END //

-- Traveller Plans Trip
CREATE PROCEDURE GetTravellerTripPlan(IN email VARCHAR(255), IN trip_id INT)
BEGIN
    SELECT * FROM Traveller_Plans_Trip WHERE email_id = email AND trip_id = trip_id;
END //

-- Trip Requires Item
CREATE PROCEDURE GetTripRequiredItem(IN trip_id INT, IN item_id INT)
BEGIN
    SELECT * FROM Trip_Requires_Item WHERE trip_id = trip_id AND item_id = item_id;
END //

-- Trip Has Destination
CREATE PROCEDURE GetTripDestination(IN dest_id INT, IN trip_id INT)
BEGIN
    SELECT * FROM Trip_Has_Destination WHERE destination_id = dest_id AND trip_id = trip_id;
END //

DELIMITER ;

-- Get	
DELIMITER //
CREATE PROCEDURE GetTripsByTravellerEmail(IN email_id VARCHAR(255))
BEGIN
    select * from trip where trip_id in (select trip_id from traveller_plans_trip where traveller_plans_trip.email_id=email_id);
END//
DELIMITER ;
