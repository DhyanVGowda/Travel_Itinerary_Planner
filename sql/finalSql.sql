drop database if exists travel_itinerary;

CREATE DATABASE travel_itinerary; 

USE travel_itinerary;

CREATE TABLE Traveller (
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

CREATE TABLE Trip (
    trip_id INT AUTO_INCREMENT PRIMARY KEY,
    trip_name VARCHAR(255) not null,
    start_date DATE,
    end_date DATE,
    trip_status enum('Planning In Progress','Planned Succesfully','Ongoing', 'Completed') not null
);

CREATE TABLE Expense (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    expense_date DATE ,
    expense_category VARCHAR(100),
    expense_description TEXT,
    amount DECIMAL(10, 2) not null,
    currency VARCHAR(10) default 'USD',
    trip_id INT,
    FOREIGN KEY (trip_id) REFERENCES Trip(trip_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Destination (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_name VARCHAR(255) not null,
    country VARCHAR(100) not null,
    arrival_date DATE ,
    departure_date DATE 
);

CREATE TABLE Activity (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    activity_location VARCHAR(255) not null,
    activity_description TEXT,
    activity_date DATE,
    start_time TIME,
    end_time TIME,
    cost DECIMAL(10, 2),
    destination_id INT,
    FOREIGN KEY (destination_id) REFERENCES Destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Activity_SightSeeing (
    activity_id INT AUTO_INCREMENT,
    site_type VARCHAR(50),
    site_description TEXT,
    FOREIGN KEY (activity_id) REFERENCES Activity(activity_id)
);

CREATE TABLE Activity_AdventureSport (
    activity_id INT AUTO_INCREMENT,
    sport_type VARCHAR(50),
    minimum_age INT,
    other_restrictions TEXT,
    FOREIGN KEY (activity_id) REFERENCES Activity(activity_id)
);

CREATE TABLE Accomodation_HomeStay (
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
    FOREIGN KEY (destination_id) REFERENCES Destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Accomodation_Hotel (
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
    FOREIGN KEY (destination_id) REFERENCES Destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Accomodation_Hostel (
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
    FOREIGN KEY (destination_id) REFERENCES Destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE EssentialPackingItems (
    item_id INT PRIMARY KEY auto_increment,
    item_name VARCHAR(255) not null
);

CREATE TABLE Traveller_Plans_Trip (
     email_id VARCHAR(255),
     trip_id INT,
     PRIMARY KEY(email_id, trip_id), 
     FOREIGN KEY (email_id) REFERENCES Traveller(email_id) ON UPDATE CASCADE ON DELETE CASCADE, 
	 FOREIGN KEY (trip_id) REFERENCES Trip(trip_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Trip_Requires_Item (
     trip_id INT,
     item_id INT,
     PRIMARY KEY(item_id, trip_id), 
     FOREIGN KEY (item_id) REFERENCES EssentialPackingItems(item_id) ON UPDATE CASCADE ON DELETE CASCADE, 
	 FOREIGN KEY (trip_id) REFERENCES Trip(trip_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Trip_Has_Destination (
     destination_id INT,
     trip_id INT,
     transportation_mode TEXT,
     travel_duration TIME,
     PRIMARY KEY(destination_id, trip_id), 
     FOREIGN KEY (destination_id) REFERENCES Destination(destination_id) ON UPDATE CASCADE ON DELETE CASCADE, 
	 FOREIGN KEY (trip_id) REFERENCES Trip(trip_id) ON UPDATE CASCADE ON DELETE CASCADE
);


