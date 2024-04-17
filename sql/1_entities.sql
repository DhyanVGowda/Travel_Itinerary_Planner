drop database if exists travel_itinerary;

CREATE DATABASE travel_itinerary; 

USE travel_itinerary;

CREATE TABLE traveller (
    email_id VARCHAR(255) PRIMARY KEY,
    mobile_number VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender VARCHAR(10),
    date_of_birth DATE,
    unit_number INT,
    street_name VARCHAR(255),
    street_number INT,
    city VARCHAR(100),
    state VARCHAR(100),
    zipcode VARCHAR(20)
);

CREATE TABLE trip (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_name VARCHAR(255) not null,
    start_date DATE,
    end_date DATE,
    trip_status enum('Planning In Progress','Planned Successfully','Ongoing', 'Completed') not null
);

CREATE TABLE expense (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE ,
    expense_category VARCHAR(100),
    expense_description TEXT,
    amount DECIMAL(10, 2) not null,
    currency VARCHAR(10) default 'USD',
    trip_id INT,
    FOREIGN KEY (trip_id) REFERENCES trip(trip_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE destination (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_name VARCHAR(255) not null,
    country VARCHAR(100) not null,
    arrival_date DATE ,
    departure_date DATE 
);

CREATE TABLE activity (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    activity_location VARCHAR(255) not null,
    activity_description TEXT,
    activity_date DATE,
    start_time TIME,
    end_time TIME,
    cost DECIMAL(10, 2),
    destination_id INT,
    FOREIGN KEY (destination_id) REFERENCES destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE activity_sightseeing (
    activity_id INT AUTO_INCREMENT,
    site_type VARCHAR(50),
    site_description TEXT,
    FOREIGN KEY (activity_id) REFERENCES activity(activity_id)
);

CREATE TABLE activity_adventuresport (
    activity_id INT AUTO_INCREMENT,
    sport_type VARCHAR(50),
    minimum_age INT,
    other_restrictions TEXT,
    FOREIGN KEY (activity_id) REFERENCES activity(activity_id)
);

CREATE TABLE accommodation_homestay (
    accommodation_id INT AUTO_INCREMENT primary key,
    accommodation_name VARCHAR(255) not null,
    cost_per_night DECIMAL(10, 2) not null,
    telephone_number VARCHAR(20) UNIQUE not null,
    checkin_date DATE,
    checkout_date DATE,
    street_name VARCHAR(255),
    street_number VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zipcode VARCHAR(20),
    destination_id INT,
    number_of_rooms INT not null,
    is_cook_available BOOLEAN,
    stay_type VARCHAR(255),
    is_pet_allowed BOOLEAN,
    FOREIGN KEY (destination_id) REFERENCES destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE accommodation_hotel (
   accommodation_id INT AUTO_INCREMENT primary key,
    accommodation_name VARCHAR(255) not null,
    cost_per_night DECIMAL(10, 2) not null,
    telephone_number VARCHAR(20) UNIQUE not null,
    checkin_date DATE,
    checkout_date DATE,
    street_name VARCHAR(255),
    street_number VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zipcode VARCHAR(20),
    destination_id INT,
    number_of_rooms INT not null,
    complimentary_meal BOOLEAN,
    star_rating enum('1','2','3','4','5'),
    FOREIGN KEY (destination_id) REFERENCES destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE accommodation_hostel (
   accommodation_id INT AUTO_INCREMENT primary key,
    accommodation_name VARCHAR(255) not null,
    cost_per_night DECIMAL(10, 2) not null,
    telephone_number VARCHAR(20) UNIQUE not null,
    checkin_date DATE,
    checkout_date DATE,
    street_name VARCHAR(255),
    street_number VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zipcode VARCHAR(20),
    destination_id INT,
    meal_service BOOLEAN,
    bathroom_type enum('Shared', 'Private'),
    free_wifi BOOLEAN,
    mixed_gender_dorm BOOLEAN,
    FOREIGN KEY (destination_id) REFERENCES destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE essential_packing_item (
    item_id INT PRIMARY KEY auto_increment,
    item_name VARCHAR(255) not null
);

CREATE TABLE traveller_plans_trip (
     email_id VARCHAR(255),
     trip_id INT,
     PRIMARY KEY(email_id, trip_id), 
     FOREIGN KEY (email_id) REFERENCES traveller(email_id) ON UPDATE CASCADE ON DELETE CASCADE,
	 FOREIGN KEY (trip_id) REFERENCES trip(trip_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE trip_requires_item (
     trip_id INT,
     item_id INT,
     PRIMARY KEY(item_id, trip_id), 
     FOREIGN KEY (item_id) REFERENCES essential_packing_item(item_id) ON UPDATE CASCADE ON DELETE CASCADE,
	 FOREIGN KEY (trip_id) REFERENCES trip(trip_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE trip_has_destination (
     destination_id INT,
     trip_id INT,
     transportation_mode TEXT,
     travel_duration TIME,
     PRIMARY KEY(destination_id, trip_id), 
     FOREIGN KEY (destination_id) REFERENCES destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE,
	 FOREIGN KEY (trip_id) REFERENCES trip(trip_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE audit_log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    table_name VARCHAR(255) NOT NULL,
    action VARCHAR(50) NOT NULL,
    record_details TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

