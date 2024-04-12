DELIMITER //
CREATE TRIGGER trg_trip_update
AFTER INSERT ON Trip
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('Trip', 'INSERT', CONCAT('Inserted trip with ID: ', NEW.trip_id, ', Name: ', NEW.trip_name), NOW());
END;
//

CREATE TRIGGER trg_trip_update
AFTER UPDATE ON Trip
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('Trip', 'UPDATE', CONCAT('Updated trip with ID: ', NEW.trip_id, ', Name: ', NEW.trip_name), NOW());
END;
//

CREATE TRIGGER trg_trip_update
AFTER DELETE ON Trip
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('Trip', 'DELETE', CONCAT('Deleted trip with ID: ', OLD.trip_id, ', Name: ', OLD.trip_name), NOW());
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER trg_traveller_insert
AFTER INSERT ON Traveller
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('Traveller', 'INSERT', CONCAT('Inserted traveller with email ID: ', NEW.email_id, ', Name: ', NEW.first_name, ' ', NEW.last_name), NOW());
END;
//

CREATE TRIGGER trg_traveller_update
AFTER UPDATE ON Traveller
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('Traveller', 'UPDATE', CONCAT('Updated traveller with email ID: ', NEW.email_id, ', Name: ', NEW.first_name, ' ', NEW.last_name), NOW());
END;
//

CREATE TRIGGER trg_traveller_delete
AFTER DELETE ON Traveller
FOR EACH ROW
BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('Traveller', 'DELETE', CONCAT('Deleted traveller with email ID: ', OLD.email_id, ', Name: ', OLD.first_name, ' ', OLD.last_name), NOW());
END;
//
DELIMITER ;


CREATE TABLE Audit_Log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(255) NOT NULL,
    action VARCHAR(50) NOT NULL,
    record_details TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);