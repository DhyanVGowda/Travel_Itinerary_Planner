DROP TRIGGER IF EXISTS trg_trip_insert;
DROP TRIGGER IF EXISTS trg_trip_update;
DROP TRIGGER IF EXISTS trg_trip_delete;
DROP TRIGGER IF EXISTS trg_traveller_insert;
DROP TRIGGER IF EXISTS trg_traveller_update;
DROP TRIGGER IF EXISTS trg_traveller_delete;

-- Change the delimiter
DELIMITER //

-- Create trigger for Trip table
CREATE TRIGGER trg_trip_insert
AFTER INSERT ON trip
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('trip', 'INSERT', CONCAT('Inserted trip with ID: ', NEW.trip_id, ', Name: ', NEW.trip_name), NOW());
END;
//

CREATE TRIGGER trg_trip_update
AFTER UPDATE ON trip
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('trip', 'UPDATE', CONCAT('Updated trip with ID: ', NEW.trip_id, ', Name: ', NEW.trip_name), NOW());
END;
//

CREATE TRIGGER trg_trip_delete
AFTER DELETE ON trip
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('trip', 'DELETE', CONCAT('Deleted trip with ID: ', OLD.trip_id, ', Name: ', OLD.trip_name), NOW());
END;
//

-- Create trigger for Traveller table
CREATE TRIGGER trg_traveller_insert
AFTER INSERT ON traveller
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('traveller', 'INSERT', CONCAT('Inserted traveller with email ID: ', NEW.email_id, ', Name: ',
    NEW.first_name, ' ', NEW.last_name), NOW());
END;
//

CREATE TRIGGER trg_traveller_update
AFTER UPDATE ON traveller
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('traveller', 'UPDATE', CONCAT('Updated traveller with email ID: ', NEW.email_id, ', Name: ', NEW.first_name,
    ' ', NEW.last_name), NOW());
END;
//

CREATE TRIGGER trg_traveller_delete
AFTER DELETE ON traveller
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('traveller', 'DELETE', CONCAT('Deleted traveller with email ID: ', OLD.email_id, ', Name: ', OLD.first_name,
    ' ', OLD.last_name), NOW());
END;
//

-- Reset delimiter to default
DELIMITER ;