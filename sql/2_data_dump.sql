-- Data for Traveller table
INSERT INTO Traveller (email_id, mobile_number, first_name, last_name, gender, date_of_birth, unit_number, street_name, street_number, city, state, zipcode) VALUES
('john.doe@email.com', '1234567870', 'John', 'Doe', 'Male', '1985-04-03', 101, 'Main St', 500, 'San Francisco', 'California', '94102'),
('jane.smith@email.com', '0987654321', 'Jane', 'Smith', 'Female', '1990-08-10', 202, 'Oak Ave', 250, 'New York', 'New York', '10001'),
('andy.blake@email.com', '5556667777', 'Andy', 'Blake', 'Male', '1979-12-22', 303, 'Second St', 1200, 'Las Vegas', 'Nevada', '88901'),
('lisa.ray@email.com', '2223334444', 'Lisa', 'Ray', 'Female', '1995-07-15', 404, 'Elm St', 800, 'Chicago', 'Illinois', '60601'),
('tom.cruise@email.com', '6667778888', 'Tom', 'Cruise', 'Male', '1980-03-14', 505, 'Pine St', 300, 'Miami', 'Florida', '33101'),
('ellen.page@email.com', '7778869999', 'Ellen', 'Page', 'Female', '1987-11-11', 606, 'Maple Ave', 700, 'Seattle', 'Washington', '98101'),
('frank.bean@email.com', '8889990000', 'Frank', 'Bean', 'Male', '1982-05-24', 707, 'Sunset Blvd', 200, 'Los Angeles', 'California', '90001'),
('nancy.grey@email.com', '9990001111', 'Nancy', 'Grey', 'Female', '1993-09-05', 808, 'Broadway', 900, 'Boston', 'Massachusetts', '02101'),
('bob.fox@email.com', '0001112222', 'Bob', 'Fox', 'Male', '1975-02-17', 909, 'Lakeview Ave', 450, 'Denver', 'Colorado', '80201'),
('sara.conor@email.com', '1112223433', 'Sara', 'Conor', 'Female', '1988-06-30', 1010, 'Hilltop Rd', 550, 'Atlanta', 'Georgia', '30301'),
('mike.stone@email.com', '3334445555', 'Mike', 'Stone', 'Male', '1992-01-23', 1111, 'Orchard Rd', 650, 'Dallas', 'Texas', '75201');

-- Data for Trip table
INSERT INTO Trip (trip_name, start_date, end_date, trip_status) VALUES
('Adventure in Yosemite', '2023-07-01', '2023-07-02', 'Planned Successfully'),
('Liberty Exploration', '2023-07-02', '2023-07-03', 'Ongoing'),
('Grand Canyon Helicopter', '2023-07-03', '2023-07-04', 'Planned Successfully'),
('Disney Dream Vacation', '2023-07-04', '2023-07-05', 'Ongoing'),
('Universal Journey', '2023-07-05', '2023-07-06', 'Planned Successfully'),
('Niagara Falls Adventure', '2023-07-06', '2023-07-07', 'Planning In Progress'),
('Paris Lights', '2023-07-07', '2023-07-08', 'Planned Successfully'),
('Great Wall Trek', '2023-07-08', '2023-07-09', 'Ongoing'),
('Sahara Nights', '2023-07-09', '2023-07-10', 'Completed'),
('Japanese Culture Tour', '2023-07-10', '2023-07-11', 'Ongoing'),
('Sydney Exploration', '2023-07-11', '2023-07-12', 'Planned Successfully');

-- Data for Expense table
INSERT INTO Expense (expense_date, expense_category, expense_description, amount, currency, trip_id) VALUES
('2023-07-01', 'Lodging', 'Hotel stay at Yosemite', 200.00, 'USD', 1),
('2023-07-02', 'Food', 'Dinner at Liberty Diner', 50.00, 'USD', 2),
('2023-07-03', 'Transportation', 'Taxi fare', 30.00, 'USD', 3),
('2023-07-04', 'Entertainment', 'Disney Park Tickets', 300.00, 'USD', 4),
('2023-07-05', 'Tours', 'Universal Studio Tour', 120.00, 'USD', 5),
('2023-07-06', 'Shopping', 'Souvenirs', 90.00, 'USD', 6),
('2023-07-07', 'Lodging', 'Night stay in Paris', 250.00, 'EUR', 7),
('2023-07-08', 'Food', 'Chinese Street Food', 40.00, 'CNY', 8),
('2023-07-09', 'Transportation', 'Camel ride in Sahara', 70.00, 'MAD', 9),
('2023-07-10', 'Entertainment', 'Kyoto Temple Entry', 15.00, 'JPY', 10),
('2023-07-11', 'Tours', 'Sydney Harbour Cruise', 85.00, 'AUD', 11);

-- Data for Destination table
INSERT INTO Destination (destination_name, country, arrival_date, departure_date) VALUES
('Yosemite National Park', 'USA', '2023-07-01', '2023-07-02'),
('Statue of Liberty', 'USA', '2023-07-02', '2023-07-03'),
('Grand Canyon', 'USA', '2023-07-03', '2023-07-04'),
('Disney World Orlando', 'USA', '2023-07-04', '2023-07-05'),
('Universal Studios', 'USA', '2023-07-05', '2023-07-06'),
('Niagara Falls', 'Canada', '2023-07-06', '2023-07-07'),
('Eiffel Tower', 'France', '2023-07-07', '2023-07-08'),
('Great Wall of China', 'China', '2023-07-08', '2023-07-09'),
('Sahara Desert', 'Morocco', '2023-07-09', '2023-07-10'),
('Kyoto Temples', 'Japan', '2023-07-10', '2023-07-11'),
('Sydney Opera House', 'Australia', '2023-07-11', '2023-07-12');

-- Data for Activity table
INSERT INTO Activity (activity_location, activity_description, activity_date, start_time, end_time, cost, destination_id) VALUES
('Yosemite National Park', 'Guided hiking tour through iconic scenic trails.', '2023-07-01', '08:00:00', '14:00:00', 50.00, 1),
('Statue of Liberty', 'Visit and explore the historical monument.', '2023-07-02', '09:00:00', '12:00:00', 25.00, 2),
('Grand Canyon', 'Helicopter tour over the canyon.', '2023-07-03', '10:00:00', '11:30:00', 300.00, 3),
('Disney World Orlando', 'Full-day access to all attractions.', '2023-07-04', '10:00:00', '20:00:00', 120.00, 4),
('Universal Studios', 'Behind-the-scenes studio tour.', '2023-07-05', '11:00:00', '16:00:00', 150.00, 5),
('Niagara Falls', 'Maid of the Mist boat tour.', '2023-07-06', '12:00:00', '13:30:00', 45.00, 6),
('Eiffel Tower', 'Skip-the-line ticket and dinner at the tower.', '2023-07-07', '19:00:00', '22:00:00', 200.00, 7),
('Great Wall of China', 'Guided walking tour of the Mutianyu section.', '2023-07-08', '09:00:00', '15:00:00', 60.00, 8),
('Sahara Desert', 'Overnight camping experience.', '2023-07-09', '17:00:00', '10:00:00', 180.00, 9),
('Kyoto Temples', 'Guided cultural tour of historic temples.', '2023-07-10', '08:00:00', '17:00:00', 70.00, 10),
('Sydney Opera House', 'Guided architectural tour.', '2023-07-11', '14:00:00', '15:30:00', 40.00, 11);

-- Data for Activity_SightSeeing table
INSERT INTO Activity_SightSeeing (activity_id, site_type, site_description) VALUES
(1, 'National Park', 'Extensive tour of Yosemite''s most famous landmarks.'),
(2, 'Monument', 'Historical insights and panoramic views.'),
(3, 'Natural Wonder', 'Breathtaking aerial views of the Grand Canyon.'),
(4, 'Amusement Park', 'Unlimited rides and entertainment.'),
(5, 'Film Studio', 'Explore famous sets and see live filming.'),
(6, 'Waterfall', 'Close-up views of the falls aboard a boat.'),
(7, 'Landmark', 'Exclusive dinner with a view of Paris by night.'),
(8, 'Historical Site', 'Learn about the history and preservation efforts.'),
(9, 'Desert', 'Star-gazing and traditional desert activities.'),
(10, 'Cultural Site', 'Explore the spiritual and historical significance.'),
(11, 'Architectural Site', 'Learn about the design and history of the opera house.');

-- Data for Activity_AdventureSport table
INSERT INTO Activity_AdventureSport (activity_id, sport_type, minimum_age, other_restrictions) VALUES
(1, 'Hiking', 12, 'Suitable for individuals with good fitness.'),
(4, 'Theme Park', 0, 'None.'),
(5, 'Studio Tour', 0, 'None.'),
(6, 'Boat Tour', 0, 'Waterproof clothing recommended.'),
(7, 'Dining Experience', 0, 'Dress code for dinner.'),
(10, 'Cultural Tour', 0, 'Respect local customs and dress modestly.'),
(11, 'Tour', 0, 'None.');

-- Data for Accommodation_HomeStay table
INSERT INTO Accommodation_Homestay (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date, street_name, street_number, city, state, zipcode, destination_id, number_of_rooms, is_cook_available, stay_type, is_pet_allowed) VALUES
('Tranquil Trails Homestay', 90.00, '9001110001', '2023-04-04', '2023-04-10', 'Trail End Rd', 101, 'Flagstaff', 'AZ', '86001', 1, 3, TRUE, 'Cottage', TRUE),
('Urban Nest', 85.00, '9001110002', '2023-04-12', '2023-04-15', 'Metropolitan Ave', 202, 'Jersey City', 'NJ', '07302', 2, 2, FALSE, 'Apartment', FALSE),
('Beachfront Bungalow', 150.00, '9001110003', '2023-04-17', '2023-04-22', 'Sandy Shore Ln', 303, 'Clearwater', 'FL', '33755', 3, 4, TRUE, 'Bungalow', TRUE),
('Forest Haven', 100.00, '9001110004', '2023-04-25', '2023-04-30', 'Pine Tree Path', 404, 'Big Sur', 'CA', '93920', 4, 3, FALSE, 'Cabin', TRUE),
('Lakeview Loft', 120.00, '9001110005', '2023-05-05', '2023-05-10', 'Lake Terrace', 505, 'Lake Placid', 'NY', '12946', 5, 2, TRUE, 'Loft', FALSE),
('Mountain Cottage', 135.00, '9001110006', '2023-05-15', '2023-05-20', 'Highland Rd', 606, 'Boulder', 'CO', '80302', 6, 3, TRUE, 'Cottage', TRUE),
('Prairie Home', 80.00, '9001110007', '2023-05-25', '2023-05-30', 'Prairie View Ln', 707, 'Wichita', 'KS', '67212', 7, 2, FALSE, 'House', FALSE),
('Riverbank Retreat', 115.00, '9001110008', '2023-06-02', '2023-06-07', 'Riverside Dr', 808, 'Knoxville', 'TN', '37902', 8, 4, TRUE, 'Retreat', TRUE),
('Old Town Studio', 75.00, '9001110009', '2023-06-12', '2023-06-17', 'Heritage Way', 909, 'Savannah', 'GA', '31401', 9, 1, FALSE, 'Studio', FALSE),
('Desert Den', 110.00, '9001110010', '2023-06-22', '2023-06-27', 'Cactus Ct', 1010, 'Santa Fe', 'NM', '87501', 10, 2, TRUE, 'Villa', TRUE),
('Garden Guesthouse', 95.00, '9001110011', '2023-07-01', '2023-07-06', 'Bloom St', 1111, 'Portland', 'OR', '97209', 11, 2, FALSE, 'Guesthouse', FALSE);

-- Data for Accommodation_Hotel table
INSERT INTO Accommodation_Hotel (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date, street_name, street_number, city, state, zipcode, destination_id, number_of_rooms, complimentary_meal, star_rating) VALUES
('Grandiose Gateway Hotel', 150.00, '8001110001', '2023-04-03', '2023-04-06', 'Gateway Blvd', 101, 'Phoenix', 'AZ', '85001', 1, 120, TRUE, 4),
('Liberty Stay', 200.00, '8001110002', '2023-04-08', '2023-04-12', 'Freedom Way', 202, 'New York', 'NY', '10001', 2, 150, TRUE, 5),
('Orlando Paradise Resort', 300.00, '8001110003', '2023-04-14', '2023-04-18', 'Disneyland Dr', 303, 'Orlando', 'FL', '32801', 3, 200, TRUE, 5),
('Alcatraz View Inn', 120.00, '8001110004', '2023-04-19', '2023-04-21', 'Alcatraz Avenue', 404, 'San Francisco', 'CA', '94111', 4, 50, FALSE, 3),
('Niagara Falls Hotel', 130.00, '8001110005', '2023-04-24', '2023-04-28', 'Waterfall Road', 505, 'Niagara Falls', 'NY', '14301', 5, 80, FALSE, 4),
('Yosemite Lodge', 250.00, '8001110006', '2023-05-02', '2023-05-06', 'National Park Dr', 606, 'Yosemite', 'CA', '95389', 6, 100, TRUE, 4),
('Yellowstone Inn', 220.00, '8001110007', '2023-05-10', '2023-05-14', 'Geysers Blvd', 707, 'Yellowstone', 'WY', '82190', 7, 90, TRUE, 4),
('Lakeside Luxury', 180.00, '8001110008', '2023-05-20', '2023-05-25', 'Lakeview Ave', 808, 'Tahoe', 'CA', '96150', 8, 70, TRUE, 4),
('Coastal View Hotel', 210.00, '8001110009', '2023-06-01', '2023-06-05', 'Ocean Blvd', 909, 'Miami', 'FL', '33101', 9, 95, TRUE, 5),
('Mountain Peak Resort', 250.00, '8001110010', '2023-06-10', '2023-06-15', 'Summit St', 1010, 'Aspen', 'CO', '81611', 10, 85, TRUE, 5),
('Urban Central Hotel', 190.00, '8001110011', '2023-06-20', '2023-06-25', 'Central Rd', 1111, 'Chicago', 'IL', '60601', 11, 120, TRUE, 4);

-- Data for Accommodation_Hostel table
INSERT INTO Accommodation_Hostel (accommodation_name, cost_per_night, telephone_number, checkin_date, checkout_date, street_name, street_number, city, state, zipcode, destination_id, meal_service, bathroom_type, free_wifi, mixed_gender_dorm) VALUES
('The Backpackers Stop', 30.00, '9011110001', '2023-04-05', '2023-04-08', 'Adventurer Ave', 101, 'Boston', 'MA', '02108', 1, FALSE, 'Shared', TRUE, TRUE),
('Nomads Nook', 25.00, '9011110002', '2023-04-10', '2023-04-14', 'Wanderer Way', 202, 'San Diego', 'CA', '92101', 2, TRUE, 'Private', TRUE, FALSE),
('City Central Hostel', 35.00, '9011110003', '2023-04-16', '2023-04-20', 'Central Station Rd', 303, 'Chicago', 'IL', '60601', 3, TRUE, 'Shared', TRUE, TRUE),
('Highland Bunkhouse', 20.00, '9011110004', '2023-04-22', '2023-04-27', 'Hilltop Rd', 404, 'Seattle', 'WA', '98101', 4, FALSE, 'Shared', FALSE, TRUE),
('Urban Hub', 28.00, '9011110005', '2023-05-01', '2023-05-05', 'Downtown Blvd', 505, 'Atlanta', 'GA', '30301', 5, TRUE, 'Private', TRUE, FALSE),
('Trailside Hostel', 22.00, '9011110006', '2023-05-10', '2023-05-14', 'Trekker Trail', 606, 'Denver', 'CO', '80201', 6, FALSE, 'Shared', TRUE, TRUE),
('Metro Mini', 27.00, '9011110007', '2023-05-19', '2023-05-23', 'Cityline Ave', 707, 'Philadelphia', 'PA', '19104', 7, TRUE, 'Private', FALSE, FALSE),
('The Loft Lodge', 32.00, '9011110008', '2023-05-28', '2023-06-02', 'Skyline St', 808, 'Las Vegas', 'NV', '89101', 8, TRUE, 'Shared', TRUE, TRUE),
('Riverside Retreat', 24.00, '9011110009', '2023-06-07', '2023-06-11', 'River Rd', 909, 'Sacramento', 'CA', '95814', 9, FALSE, 'Shared', TRUE, TRUE),
('The Cosmopolitan', 33.00, '9011110010', '2023-06-15', '2023-06-20', 'Vogue Ave', 1010, 'Manhattan', 'NY', '10001', 10, TRUE, 'Private', TRUE, FALSE),
('The Nomadic', 29.00, '9011110011', '2023-06-25', '2023-06-30', 'Nomad St', 1111, 'Austin', 'TX', '78701', 11, FALSE, 'Shared', TRUE, TRUE);

-- Data for EssentialPackingItems table
INSERT INTO essential_packing_item (item_name) VALUES
('Waterproof Jacket'),
('Travel Adapter'),
('Sunscreen'),
('Hiking Boots'),
('First Aid Kit'),
('Insect Repellent'),
('Camera'),
('Hat'),
('Sunglasses'),
('Portable Charger'),
('Travel Pillow');

-- Data for Traveller_Plans_Trip table
INSERT INTO Traveller_Plans_Trip (email_id, trip_id) VALUES
('john.doe@email.com', 1),
('jane.smith@email.com', 2),
('andy.blake@email.com', 3),
('lisa.ray@email.com', 4),
('tom.cruise@email.com', 5),
('ellen.page@email.com', 6),
('frank.bean@email.com', 7),
('nancy.grey@email.com', 8),
('bob.fox@email.com', 9),
('sara.conor@email.com', 10),
('mike.stone@email.com', 11);

-- Data for Trip_Requires_Item table
INSERT INTO Trip_Requires_Item (trip_id, item_id) VALUES
(1, 4),
(2, 2),  -- Travel Adapter for Liberty
(3, 4),  -- Hiking Boots for Grand Canyon
(4, 5),  -- First Aid Kit for Disney World
(5, 3),  -- Sunscreen for Universal Studios
(6, 6),  -- Insect Repellent for Niagara Falls
(7, 8),  -- Hat for Eiffel Tower
(8, 7),  -- Camera for Great Wall
(9, 9),  -- Sunglasses for Sahara
(10, 10), -- Portable Charger for Kyoto
(11, 11); -- Travel Pillow for Sydney

-- Data for Trip_Has_Destination table
INSERT INTO Trip_Has_Destination (destination_id, trip_id, transportation_mode, travel_duration) VALUES
(1, 6, 'Car', '02:00:00'),   
(2, 4, 'Ferry', '00:30:00'),  
(3, 5, 'Helicopter', '00:15:00'), 
(4, 3, 'Bus', '01:00:00'),    
(5, 8, 'Tram', '00:20:00'),   
(6, 6, 'Boat', '00:30:00'),   
(7, 7, 'Metro', '00:10:00'),  
(8, 8, 'Walk', '03:00:00'),   
(9, 9, '4x4', '04:00:00'),    
(10, 10, 'Bus', '02:00:00'),  
(11, 11, 'Ferry', '00:45:00');