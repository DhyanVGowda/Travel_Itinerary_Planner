-- Trigger 1: Example trigger on the Traveller table
DELIMITER //
CREATE TRIGGER trg_traveller_insert
AFTER INSERT ON Traveller
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    INSERT INTO Audit_Trail (table_name, action, timestamp)
    VALUES ('Traveller', 'INSERT', NOW());
END;
//
DELIMITER ;

-- Trigger 2: Example trigger on the Trip table
DELIMITER //
CREATE TRIGGER trg_trip_update
BEFORE UPDATE ON Trip
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    UPDATE Audit_Log SET last_updated = NOW() WHERE table_name = 'Trip';
END;
//
DELIMITER ;

-- Trigger 3: Example trigger on the Expense table
DELIMITER //
CREATE TRIGGER trg_expense_delete
BEFORE DELETE ON Expense
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    INSERT INTO Deleted_Records (table_name, record_id, deleted_at)
    VALUES ('Expense', OLD.expense_id, NOW());
END;
//
DELIMITER ;

-- Trigger 4: Example trigger on the Destination table
DELIMITER //
CREATE TRIGGER trg_destination_insert
AFTER INSERT ON Destination
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    INSERT INTO Audit_Log (table_name, action, timestamp)
    VALUES ('Destination', 'INSERT', NOW());
END;
//
DELIMITER ;

-- Trigger 5: Example trigger on the Activity table
DELIMITER //
CREATE TRIGGER trg_activity_update
BEFORE UPDATE ON Activity
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    UPDATE Audit_Trail SET action = 'UPDATE' WHERE table_name = 'Activity';
END;
//
DELIMITER ;

-- Trigger 6: Example trigger on the Activity_SightSeeing table
DELIMITER //
CREATE TRIGGER trg_activity_sightseeing_insert
AFTER INSERT ON Activity_SightSeeing
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    INSERT INTO Audit_Log (table_name, action, timestamp)
    VALUES ('Activity_SightSeeing', 'INSERT', NOW());
END;
//
DELIMITER ;

-- Trigger 7: Example trigger on the Accommodation_HomeStay table
DELIMITER //
CREATE TRIGGER trg_accommodation_homestay_update
BEFORE UPDATE ON Accommodation_HomeStay
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    UPDATE Audit_Trail SET last_updated = NOW() WHERE table_name = 'Accommodation_HomeStay';
END;
//
DELIMITER ;

-- Trigger 8: Example trigger on the Accommodation_Hotel table
DELIMITER //
CREATE TRIGGER trg_accommodation_hotel_delete
BEFORE DELETE ON Accommodation_Hotel
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    INSERT INTO Deleted_Records (table_name, record_id, deleted_at)
    VALUES ('Accommodation_Hotel', OLD.accommodation_id, NOW());
END;
//
DELIMITER ;

-- Trigger 9: Example trigger on the Accommodation_Hostel table
DELIMITER //
CREATE TRIGGER trg_accommodation_hostel_insert
AFTER INSERT ON Accommodation_Hostel
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    INSERT INTO Audit_Log (table_name, action, timestamp)
    VALUES ('Accommodation_Hostel', 'INSERT', NOW());
END;
//
DELIMITER ;

-- Trigger 10: Example trigger on the EssentialPackingItems table
DELIMITER //
CREATE TRIGGER trg_essential_items_delete
BEFORE DELETE ON EssentialPackingItems
FOR EACH ROW
BEGIN
    -- Trigger action (example)
    INSERT INTO Deleted_Records (table_name, record_id, deleted_at)
    VALUES ('EssentialPackingItems', OLD.item_id, NOW());
END;
//
DELIMITER ;
