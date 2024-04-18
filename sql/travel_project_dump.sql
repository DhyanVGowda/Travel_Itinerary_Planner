CREATE DATABASE  IF NOT EXISTS `travel_itinerary` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `travel_itinerary`;
-- MySQL dump 10.13  Distrib 8.0.36, for macos14 (arm64)
--
-- Host: 127.0.0.1    Database: travel_itinerary
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accommodation_homestay`
--

DROP TABLE IF EXISTS `accommodation_homestay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accommodation_homestay` (
  `accommodation_id` int NOT NULL AUTO_INCREMENT,
  `accommodation_name` varchar(255) NOT NULL,
  `cost_per_night` decimal(10,2) NOT NULL,
  `telephone_number` varchar(20) NOT NULL,
  `checkin_date` date DEFAULT NULL,
  `checkout_date` date DEFAULT NULL,
  `street_name` varchar(255) DEFAULT NULL,
  `street_number` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `zipcode` varchar(20) DEFAULT NULL,
  `destination_id` int DEFAULT NULL,
  `number_of_rooms` int NOT NULL,
  `is_cook_available` tinyint(1) DEFAULT NULL,
  `stay_type` varchar(255) DEFAULT NULL,
  `is_pet_allowed` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`accommodation_id`),
  UNIQUE KEY `telephone_number` (`telephone_number`),
  KEY `destination_id` (`destination_id`),
  CONSTRAINT `accommodation_homestay_ibfk_1` FOREIGN KEY (`destination_id`) REFERENCES `destination` (`destination_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accommodation_homestay`
--

LOCK TABLES `accommodation_homestay` WRITE;
/*!40000 ALTER TABLE `accommodation_homestay` DISABLE KEYS */;
INSERT INTO `accommodation_homestay` VALUES (1,'Tranquil Trails Homestay',90.00,'9001110001','2023-04-04','2023-04-10','Trail End Rd','101','Flagstaff','AZ','86001',1,3,1,'Cottage',1),(2,'Urban Nest',85.00,'9001110002','2023-04-12','2023-04-15','Metropolitan Ave','202','Jersey City','NJ','07302',2,2,0,'Apartment',0),(3,'Beachfront Bungalow',150.00,'9001110003','2023-04-17','2023-04-22','Sandy Shore Ln','303','Clearwater','FL','33755',3,4,1,'Bungalow',1),(4,'Forest Haven',100.00,'9001110004','2023-04-25','2023-04-30','Pine Tree Path','404','Big Sur','CA','93920',4,3,0,'Cabin',1),(5,'Lakeview Loft',120.00,'9001110005','2023-05-05','2023-05-10','Lake Terrace','505','Lake Placid','NY','12946',5,2,1,'Loft',0),(6,'Mountain Cottage',135.00,'9001110006','2023-05-15','2023-05-20','Highland Rd','606','Boulder','CO','80302',6,3,1,'Cottage',1),(7,'Prairie Home',80.00,'9001110007','2023-05-25','2023-05-30','Prairie View Ln','707','Wichita','KS','67212',7,2,0,'House',0),(8,'Riverbank Retreat',115.00,'9001110008','2023-06-02','2023-06-07','Riverside Dr','808','Knoxville','TN','37902',8,4,1,'Retreat',1),(9,'Old Town Studio',75.00,'9001110009','2023-06-12','2023-06-17','Heritage Way','909','Savannah','GA','31401',9,1,0,'Studio',0),(10,'Desert Den',110.00,'9001110010','2023-06-22','2023-06-27','Cactus Ct','1010','Santa Fe','NM','87501',10,2,1,'Villa',1),(11,'Garden Guesthouse',95.00,'9001110011','2023-07-01','2023-07-06','Bloom St','1111','Portland','OR','97209',11,2,0,'Guesthouse',0);
/*!40000 ALTER TABLE `accommodation_homestay` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accommodation_hostel`
--

DROP TABLE IF EXISTS `accommodation_hostel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accommodation_hostel` (
  `accommodation_id` int NOT NULL AUTO_INCREMENT,
  `accommodation_name` varchar(255) NOT NULL,
  `cost_per_night` decimal(10,2) NOT NULL,
  `telephone_number` varchar(20) NOT NULL,
  `checkin_date` date DEFAULT NULL,
  `checkout_date` date DEFAULT NULL,
  `street_name` varchar(255) DEFAULT NULL,
  `street_number` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `zipcode` varchar(20) DEFAULT NULL,
  `destination_id` int DEFAULT NULL,
  `meal_service` tinyint(1) DEFAULT NULL,
  `bathroom_type` enum('Shared','Private') DEFAULT NULL,
  `free_wifi` tinyint(1) DEFAULT NULL,
  `mixed_gender_dorm` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`accommodation_id`),
  UNIQUE KEY `telephone_number` (`telephone_number`),
  KEY `destination_id` (`destination_id`),
  CONSTRAINT `accommodation_hostel_ibfk_1` FOREIGN KEY (`destination_id`) REFERENCES `destination` (`destination_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accommodation_hostel`
--

LOCK TABLES `accommodation_hostel` WRITE;
/*!40000 ALTER TABLE `accommodation_hostel` DISABLE KEYS */;
INSERT INTO `accommodation_hostel` VALUES (1,'The Backpackers Stop',30.00,'9011110001','2023-04-05','2023-04-08','Adventurer Ave','101','Boston','MA','02108',1,0,'Shared',1,1),(2,'Nomads Nook',25.00,'9011110002','2023-04-10','2023-04-14','Wanderer Way','202','San Diego','CA','92101',2,1,'Private',1,0),(3,'City Central Hostel',35.00,'9011110003','2023-04-16','2023-04-20','Central Station Rd','303','Chicago','IL','60601',3,1,'Shared',1,1),(4,'Highland Bunkhouse',20.00,'9011110004','2023-04-22','2023-04-27','Hilltop Rd','404','Seattle','WA','98101',4,0,'Shared',0,1),(5,'Urban Hub',28.00,'9011110005','2023-05-01','2023-05-05','Downtown Blvd','505','Atlanta','GA','30301',5,1,'Private',1,0),(6,'Trailside Hostel',22.00,'9011110006','2023-05-10','2023-05-14','Trekker Trail','606','Denver','CO','80201',6,0,'Shared',1,1),(7,'Metro Mini',27.00,'9011110007','2023-05-19','2023-05-23','Cityline Ave','707','Philadelphia','PA','19104',7,1,'Private',0,0),(8,'The Loft Lodge',32.00,'9011110008','2023-05-28','2023-06-02','Skyline St','808','Las Vegas','NV','89101',8,1,'Shared',1,1),(9,'Riverside Retreat',24.00,'9011110009','2023-06-07','2023-06-11','River Rd','909','Sacramento','CA','95814',9,0,'Shared',1,1),(10,'The Cosmopolitan',33.00,'9011110010','2023-06-15','2023-06-20','Vogue Ave','1010','Manhattan','NY','10001',10,1,'Private',1,0),(11,'The Nomadic',29.00,'9011110011','2023-06-25','2023-06-30','Nomad St','1111','Austin','TX','78701',11,0,'Shared',1,1);
/*!40000 ALTER TABLE `accommodation_hostel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accommodation_hotel`
--

DROP TABLE IF EXISTS `accommodation_hotel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accommodation_hotel` (
  `accommodation_id` int NOT NULL AUTO_INCREMENT,
  `accommodation_name` varchar(255) NOT NULL,
  `cost_per_night` decimal(10,2) NOT NULL,
  `telephone_number` varchar(20) NOT NULL,
  `checkin_date` date DEFAULT NULL,
  `checkout_date` date DEFAULT NULL,
  `street_name` varchar(255) DEFAULT NULL,
  `street_number` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `zipcode` varchar(20) DEFAULT NULL,
  `destination_id` int DEFAULT NULL,
  `number_of_rooms` int NOT NULL,
  `complimentary_meal` tinyint(1) DEFAULT NULL,
  `star_rating` enum('1','2','3','4','5') DEFAULT NULL,
  PRIMARY KEY (`accommodation_id`),
  UNIQUE KEY `telephone_number` (`telephone_number`),
  KEY `destination_id` (`destination_id`),
  CONSTRAINT `accommodation_hotel_ibfk_1` FOREIGN KEY (`destination_id`) REFERENCES `destination` (`destination_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accommodation_hotel`
--

LOCK TABLES `accommodation_hotel` WRITE;
/*!40000 ALTER TABLE `accommodation_hotel` DISABLE KEYS */;
INSERT INTO `accommodation_hotel` VALUES (1,'Grandiose Gateway Hotel',150.00,'8001110001','2023-04-03','2023-04-06','Gateway Blvd','101','Phoenix','AZ','85001',1,120,1,'4'),(2,'Liberty Stay',200.00,'8001110002','2023-04-08','2023-04-12','Freedom Way','202','New York','NY','10001',2,150,1,'5'),(3,'Orlando Paradise Resort',300.00,'8001110003','2023-04-14','2023-04-18','Disneyland Dr','303','Orlando','FL','32801',3,200,1,'5'),(4,'Alcatraz View Inn',120.00,'8001110004','2023-04-19','2023-04-21','Alcatraz Avenue','404','San Francisco','CA','94111',4,50,0,'3'),(5,'Niagara Falls Hotel',130.00,'8001110005','2023-04-24','2023-04-28','Waterfall Road','505','Niagara Falls','NY','14301',5,80,0,'4'),(6,'Yosemite Lodge',250.00,'8001110006','2023-05-02','2023-05-06','National Park Dr','606','Yosemite','CA','95389',6,100,1,'4'),(7,'Yellowstone Inn',220.00,'8001110007','2023-05-10','2023-05-14','Geysers Blvd','707','Yellowstone','WY','82190',7,90,1,'4'),(8,'Lakeside Luxury',180.00,'8001110008','2023-05-20','2023-05-25','Lakeview Ave','808','Tahoe','CA','96150',8,70,1,'4'),(9,'Coastal View Hotel',210.00,'8001110009','2023-06-01','2023-06-05','Ocean Blvd','909','Miami','FL','33101',9,95,1,'5'),(10,'Mountain Peak Resort',250.00,'8001110010','2023-06-10','2023-06-15','Summit St','1010','Aspen','CO','81611',10,85,1,'5'),(11,'Urban Central Hotel',190.00,'8001110011','2023-06-20','2023-06-25','Central Rd','1111','Chicago','IL','60601',11,120,1,'4');
/*!40000 ALTER TABLE `accommodation_hotel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `activity`
--

DROP TABLE IF EXISTS `activity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activity` (
  `activity_id` int NOT NULL AUTO_INCREMENT,
  `activity_location` varchar(255) NOT NULL,
  `activity_description` text,
  `activity_date` date DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `cost` decimal(10,2) DEFAULT NULL,
  `destination_id` int DEFAULT NULL,
  PRIMARY KEY (`activity_id`),
  KEY `destination_id` (`destination_id`),
  CONSTRAINT `activity_ibfk_1` FOREIGN KEY (`destination_id`) REFERENCES `destination` (`destination_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity`
--

LOCK TABLES `activity` WRITE;
/*!40000 ALTER TABLE `activity` DISABLE KEYS */;
INSERT INTO `activity` VALUES (1,'Yosemite National Park','Guided hiking tour through iconic scenic trails.','2023-07-01','08:00:00','14:00:00',50.00,1),(2,'Statue of Liberty','Visit and explore the historical monument.','2023-07-02','09:00:00','12:00:00',25.00,2),(3,'Grand Canyon','Helicopter tour over the canyon.','2023-07-03','10:00:00','11:30:00',300.00,3),(4,'Disney World Orlando','Full-day access to all attractions.','2023-07-04','10:00:00','20:00:00',120.00,4),(5,'Universal Studios','Behind-the-scenes studio tour.','2023-07-05','11:00:00','16:00:00',150.00,5),(6,'Niagara Falls','Maid of the Mist boat tour.','2023-07-06','12:00:00','13:30:00',45.00,6),(7,'Eiffel Tower','Skip-the-line ticket and dinner at the tower.','2023-07-07','19:00:00','22:00:00',200.00,7),(8,'Great Wall of China','Guided walking tour of the Mutianyu section.','2023-07-08','09:00:00','15:00:00',60.00,8),(9,'Sahara Desert','Overnight camping experience.','2023-07-09','17:00:00','10:00:00',180.00,9),(10,'Kyoto Temples','Guided cultural tour of historic temples.','2023-07-10','08:00:00','17:00:00',70.00,10),(11,'Sydney Opera House','Guided architectural tour.','2023-07-11','14:00:00','15:30:00',40.00,11);
/*!40000 ALTER TABLE `activity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `activity_adventuresport`
--

DROP TABLE IF EXISTS `activity_adventuresport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activity_adventuresport` (
  `activity_id` int NOT NULL AUTO_INCREMENT,
  `sport_type` varchar(50) DEFAULT NULL,
  `minimum_age` int DEFAULT NULL,
  `other_restrictions` text,
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `activity_adventuresport_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`activity_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity_adventuresport`
--

LOCK TABLES `activity_adventuresport` WRITE;
/*!40000 ALTER TABLE `activity_adventuresport` DISABLE KEYS */;
INSERT INTO `activity_adventuresport` VALUES (1,'Hiking',12,'Suitable for individuals with good fitness.'),(4,'Theme Park',0,'None.'),(5,'Studio Tour',0,'None.'),(6,'Boat Tour',0,'Waterproof clothing recommended.'),(7,'Dining Experience',0,'Dress code for dinner.'),(10,'Cultural Tour',0,'Respect local customs and dress modestly.'),(11,'Tour',0,'None.');
/*!40000 ALTER TABLE `activity_adventuresport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `activity_sightseeing`
--

DROP TABLE IF EXISTS `activity_sightseeing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `activity_sightseeing` (
  `activity_id` int NOT NULL AUTO_INCREMENT,
  `site_type` varchar(50) DEFAULT NULL,
  `site_description` text,
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `activity_sightseeing_ibfk_1` FOREIGN KEY (`activity_id`) REFERENCES `activity` (`activity_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activity_sightseeing`
--

LOCK TABLES `activity_sightseeing` WRITE;
/*!40000 ALTER TABLE `activity_sightseeing` DISABLE KEYS */;
INSERT INTO `activity_sightseeing` VALUES (1,'National Park','Extensive tour of Yosemite\'s most famous landmarks.'),(2,'Monument','Historical insights and panoramic views.'),(3,'Natural Wonder','Breathtaking aerial views of the Grand Canyon.'),(4,'Amusement Park','Unlimited rides and entertainment.'),(5,'Film Studio','Explore famous sets and see live filming.'),(6,'Waterfall','Close-up views of the falls aboard a boat.'),(7,'Landmark','Exclusive dinner with a view of Paris by night.'),(8,'Historical Site','Learn about the history and preservation efforts.'),(9,'Desert','Star-gazing and traditional desert activities.'),(10,'Cultural Site','Explore the spiritual and historical significance.'),(11,'Architectural Site','Learn about the design and history of the opera house.');
/*!40000 ALTER TABLE `activity_sightseeing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_log`
--

DROP TABLE IF EXISTS `audit_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audit_log` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `table_name` varchar(255) NOT NULL,
  `action` varchar(50) NOT NULL,
  `record_details` text,
  `timestamp` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_log`
--

LOCK TABLES `audit_log` WRITE;
/*!40000 ALTER TABLE `audit_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `audit_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `destination`
--

DROP TABLE IF EXISTS `destination`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `destination` (
  `destination_id` int NOT NULL AUTO_INCREMENT,
  `destination_name` varchar(255) NOT NULL,
  `country` varchar(100) NOT NULL,
  `arrival_date` date DEFAULT NULL,
  `departure_date` date DEFAULT NULL,
  PRIMARY KEY (`destination_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destination`
--

LOCK TABLES `destination` WRITE;
/*!40000 ALTER TABLE `destination` DISABLE KEYS */;
INSERT INTO `destination` VALUES (1,'Yosemite National Park','USA','2023-07-01','2023-07-02'),(2,'Statue of Liberty','USA','2023-07-02','2023-07-03'),(3,'Grand Canyon','USA','2023-07-03','2023-07-04'),(4,'Disney World Orlando','USA','2023-07-04','2023-07-05'),(5,'Universal Studios','USA','2023-07-05','2023-07-06'),(6,'Niagara Falls','Canada','2023-07-06','2023-07-07'),(7,'Eiffel Tower','France','2023-07-07','2023-07-08'),(8,'Great Wall of China','China','2023-07-08','2023-07-09'),(9,'Sahara Desert','Morocco','2023-07-09','2023-07-10'),(10,'Kyoto Temples','Japan','2023-07-10','2023-07-11'),(11,'Sydney Opera House','Australia','2023-07-11','2023-07-12');
/*!40000 ALTER TABLE `destination` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `essential_packing_item`
--

DROP TABLE IF EXISTS `essential_packing_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `essential_packing_item` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) NOT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `essential_packing_item`
--

LOCK TABLES `essential_packing_item` WRITE;
/*!40000 ALTER TABLE `essential_packing_item` DISABLE KEYS */;
INSERT INTO `essential_packing_item` VALUES (1,'Waterproof Jacket'),(2,'Travel Adapter'),(3,'Sunscreen'),(4,'Hiking Boots'),(5,'First Aid Kit'),(6,'Insect Repellent'),(7,'Camera'),(8,'Hat'),(9,'Sunglasses'),(10,'Portable Charger'),(11,'Travel Pillow');
/*!40000 ALTER TABLE `essential_packing_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expense`
--

DROP TABLE IF EXISTS `expense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expense` (
  `expense_id` int NOT NULL AUTO_INCREMENT,
  `expense_date` date DEFAULT NULL,
  `expense_category` varchar(100) DEFAULT NULL,
  `expense_description` text,
  `amount` decimal(10,2) NOT NULL,
  `currency` varchar(10) DEFAULT 'USD',
  `trip_id` int DEFAULT NULL,
  PRIMARY KEY (`expense_id`),
  KEY `trip_id` (`trip_id`),
  CONSTRAINT `expense_ibfk_1` FOREIGN KEY (`trip_id`) REFERENCES `trip` (`trip_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expense`
--

LOCK TABLES `expense` WRITE;
/*!40000 ALTER TABLE `expense` DISABLE KEYS */;
INSERT INTO `expense` VALUES (1,'2023-07-01','Lodging','Hotel stay at Yosemite',200.00,'USD',1),(2,'2023-07-02','Food','Dinner at Liberty Diner',50.00,'USD',2),(3,'2023-07-03','Transportation','Taxi fare',30.00,'USD',3),(4,'2023-07-04','Entertainment','Disney Park Tickets',300.00,'USD',4),(5,'2023-07-05','Tours','Universal Studio Tour',120.00,'USD',5),(6,'2023-07-06','Shopping','Souvenirs',90.00,'USD',6),(7,'2023-07-07','Lodging','Night stay in Paris',250.00,'EUR',7),(8,'2023-07-08','Food','Chinese Street Food',40.00,'CNY',8),(9,'2023-07-09','Transportation','Camel ride in Sahara',70.00,'MAD',9),(10,'2023-07-10','Entertainment','Kyoto Temple Entry',15.00,'JPY',10),(11,'2023-07-11','Tours','Sydney Harbour Cruise',85.00,'AUD',11);
/*!40000 ALTER TABLE `expense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `traveller`
--

DROP TABLE IF EXISTS `traveller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `traveller` (
  `email_id` varchar(255) NOT NULL,
  `mobile_number` varchar(20) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `unit_number` int DEFAULT NULL,
  `street_name` varchar(255) DEFAULT NULL,
  `street_number` int DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `zipcode` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`email_id`),
  UNIQUE KEY `mobile_number` (`mobile_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `traveller`
--

LOCK TABLES `traveller` WRITE;
/*!40000 ALTER TABLE `traveller` DISABLE KEYS */;
INSERT INTO `traveller` VALUES ('andy.blake@email.com','5556667777','Andy','Blake','Male','1979-12-22',303,'Second St',1200,'Las Vegas','Nevada','88901'),('bob.fox@email.com','0001112222','Bob','Fox','Male','1975-02-17',909,'Lakeview Ave',450,'Denver','Colorado','80201'),('ellen.page@email.com','7778869999','Ellen','Page','Female','1987-11-11',606,'Maple Ave',700,'Seattle','Washington','98101'),('frank.bean@email.com','8889990000','Frank','Bean','Male','1982-05-24',707,'Sunset Blvd',200,'Los Angeles','California','90001'),('jane.smith@email.com','0987654321','Jane','Smith','Female','1990-08-10',202,'Oak Ave',250,'New York','New York','10001'),('john.doe@email.com','1234567870','John','Doe','Male','1985-04-03',101,'Main St',500,'San Francisco','California','94102'),('lisa.ray@email.com','2223334444','Lisa','Ray','Female','1995-07-15',404,'Elm St',800,'Chicago','Illinois','60601'),('mike.stone@email.com','3334445555','Mike','Stone','Male','1992-01-23',1111,'Orchard Rd',650,'Dallas','Texas','75201'),('nancy.grey@email.com','9990001111','Nancy','Grey','Female','1993-09-05',808,'Broadway',900,'Boston','Massachusetts','02101'),('sara.conor@email.com','1112223433','Sara','Conor','Female','1988-06-30',1010,'Hilltop Rd',550,'Atlanta','Georgia','30301'),('tom.cruise@email.com','6667778888','Tom','Cruise','Male','1980-03-14',505,'Pine St',300,'Miami','Florida','33101');
/*!40000 ALTER TABLE `traveller` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `trg_traveller_insert` AFTER INSERT ON `traveller` FOR EACH ROW BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('traveller', 'INSERT', CONCAT('Inserted traveller with email ID: ', NEW.email_id, ', Name: ',
    NEW.first_name, ' ', NEW.last_name), NOW());
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `trg_traveller_update` AFTER UPDATE ON `traveller` FOR EACH ROW BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('traveller', 'UPDATE', CONCAT('Updated traveller with email ID: ', NEW.email_id, ', Name: ', NEW.first_name,
    ' ', NEW.last_name), NOW());
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `trg_traveller_delete` AFTER DELETE ON `traveller` FOR EACH ROW BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('traveller', 'DELETE', CONCAT('Deleted traveller with email ID: ', OLD.email_id, ', Name: ', OLD.first_name,
    ' ', OLD.last_name), NOW());
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `traveller_plans_trip`
--

DROP TABLE IF EXISTS `traveller_plans_trip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `traveller_plans_trip` (
  `email_id` varchar(255) NOT NULL,
  `trip_id` int NOT NULL,
  PRIMARY KEY (`email_id`,`trip_id`),
  KEY `trip_id` (`trip_id`),
  CONSTRAINT `traveller_plans_trip_ibfk_1` FOREIGN KEY (`email_id`) REFERENCES `traveller` (`email_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `traveller_plans_trip_ibfk_2` FOREIGN KEY (`trip_id`) REFERENCES `trip` (`trip_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `traveller_plans_trip`
--

LOCK TABLES `traveller_plans_trip` WRITE;
/*!40000 ALTER TABLE `traveller_plans_trip` DISABLE KEYS */;
INSERT INTO `traveller_plans_trip` VALUES ('john.doe@email.com',1),('jane.smith@email.com',2),('andy.blake@email.com',3),('lisa.ray@email.com',4),('tom.cruise@email.com',5),('ellen.page@email.com',6),('frank.bean@email.com',7),('nancy.grey@email.com',8),('bob.fox@email.com',9),('sara.conor@email.com',10),('mike.stone@email.com',11);
/*!40000 ALTER TABLE `traveller_plans_trip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trip`
--

DROP TABLE IF EXISTS `trip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trip` (
  `trip_id` int NOT NULL AUTO_INCREMENT,
  `trip_name` varchar(255) NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `trip_status` enum('Planning In Progress','Planned Successfully','Ongoing','Completed') NOT NULL,
  PRIMARY KEY (`trip_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trip`
--

LOCK TABLES `trip` WRITE;
/*!40000 ALTER TABLE `trip` DISABLE KEYS */;
INSERT INTO `trip` VALUES (1,'Adventure in Yosemite','2023-07-01','2023-07-02','Planned Successfully'),(2,'Liberty Exploration','2023-07-02','2023-07-03','Ongoing'),(3,'Grand Canyon Helicopter','2023-07-03','2023-07-04','Planned Successfully'),(4,'Disney Dream Vacation','2023-07-04','2023-07-05','Ongoing'),(5,'Universal Journey','2023-07-05','2023-07-06','Planned Successfully'),(6,'Niagara Falls Adventure','2023-07-06','2023-07-07','Planning In Progress'),(7,'Paris Lights','2023-07-07','2023-07-08','Planned Successfully'),(8,'Great Wall Trek','2023-07-08','2023-07-09','Ongoing'),(9,'Sahara Nights','2023-07-09','2023-07-10','Completed'),(10,'Japanese Culture Tour','2023-07-10','2023-07-11','Ongoing'),(11,'Sydney Exploration','2023-07-11','2023-07-12','Planned Successfully');
/*!40000 ALTER TABLE `trip` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `trg_trip_insert` AFTER INSERT ON `trip` FOR EACH ROW BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('trip', 'INSERT', CONCAT('Inserted trip with ID: ', NEW.trip_id, ', Name: ', NEW.trip_name), NOW());
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `trg_trip_update` AFTER UPDATE ON `trip` FOR EACH ROW BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('trip', 'UPDATE', CONCAT('Updated trip with ID: ', NEW.trip_id, ', Name: ', NEW.trip_name), NOW());
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `trg_trip_delete` AFTER DELETE ON `trip` FOR EACH ROW BEGIN
    -- Inserting the record details into the Audit_Log table
    INSERT INTO Audit_Log (table_name, action, record_details, timestamp)
    VALUES ('trip', 'DELETE', CONCAT('Deleted trip with ID: ', OLD.trip_id, ', Name: ', OLD.trip_name), NOW());
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `trip_has_destination`
--

DROP TABLE IF EXISTS `trip_has_destination`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trip_has_destination` (
  `destination_id` int NOT NULL,
  `trip_id` int NOT NULL,
  `transportation_mode` text,
  `travel_duration` time DEFAULT NULL,
  PRIMARY KEY (`destination_id`,`trip_id`),
  KEY `trip_id` (`trip_id`),
  CONSTRAINT `trip_has_destination_ibfk_1` FOREIGN KEY (`destination_id`) REFERENCES `destination` (`destination_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `trip_has_destination_ibfk_2` FOREIGN KEY (`trip_id`) REFERENCES `trip` (`trip_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trip_has_destination`
--

LOCK TABLES `trip_has_destination` WRITE;
/*!40000 ALTER TABLE `trip_has_destination` DISABLE KEYS */;
INSERT INTO `trip_has_destination` VALUES (1,6,'Car','02:00:00'),(2,4,'Ferry','00:30:00'),(3,5,'Helicopter','00:15:00'),(4,3,'Bus','01:00:00'),(5,8,'Tram','00:20:00'),(6,6,'Boat','00:30:00'),(7,7,'Metro','00:10:00'),(8,8,'Walk','03:00:00'),(9,9,'4x4','04:00:00'),(10,10,'Bus','02:00:00'),(11,11,'Ferry','00:45:00');
/*!40000 ALTER TABLE `trip_has_destination` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trip_requires_item`
--

DROP TABLE IF EXISTS `trip_requires_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trip_requires_item` (
  `trip_id` int NOT NULL,
  `item_id` int NOT NULL,
  PRIMARY KEY (`item_id`,`trip_id`),
  KEY `trip_id` (`trip_id`),
  CONSTRAINT `trip_requires_item_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `essential_packing_item` (`item_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `trip_requires_item_ibfk_2` FOREIGN KEY (`trip_id`) REFERENCES `trip` (`trip_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trip_requires_item`
--

LOCK TABLES `trip_requires_item` WRITE;
/*!40000 ALTER TABLE `trip_requires_item` DISABLE KEYS */;
INSERT INTO `trip_requires_item` VALUES (1,4),(2,2),(3,4),(4,5),(5,3),(6,6),(7,8),(8,7),(9,9),(10,10),(11,11);
/*!40000 ALTER TABLE `trip_requires_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'travel_itinerary'
--
/*!50003 DROP PROCEDURE IF EXISTS `add_activity` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_activity`(
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
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_adventuresport_activity` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_adventuresport_activity`(
     IN act_id INT,
     IN sport_type VARCHAR(50),
     IN min_age INT,
     IN restrictions TEXT
 )
BEGIN
     INSERT INTO activity_adventuresport (activity_id, sport_type, minimum_age, other_restrictions)
     VALUES (act_id, sport_type, min_age, restrictions);
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_destination` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_destination`(
     IN dest_name VARCHAR(255),
     IN cntry VARCHAR(100),
     IN arr_date DATE,
     IN dep_date DATE
 )
BEGIN
     INSERT INTO destination (destination_name, country, arrival_date, departure_date)
     VALUES (dest_name, cntry, arr_date, dep_date);
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_essential_packing_item` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_essential_packing_item`(
     IN item_name VARCHAR(255)
 )
BEGIN
     INSERT INTO essential_packing_item (item_name)
     VALUES (item_name);
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_expense` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_expense`(
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
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_homestay_accommodation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_homestay_accommodation`(
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
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_hostel_accommodation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_hostel_accommodation`(
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
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_hotel_accommodation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_hotel_accommodation`(
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
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_sightseeing_activity` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_sightseeing_activity`(
     IN act_id INT,
     IN site_type VARCHAR(50),
     IN site_description TEXT
 )
BEGIN
     INSERT INTO activity_sightseeing (activity_id, site_type, site_description)
     VALUES (act_id, site_type, site_description);
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_traveller` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_traveller`(
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_traveller_trip_plan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_traveller_trip_plan`(
    IN email VARCHAR(255),
    IN trip_id INT
)
BEGIN
    INSERT INTO traveller_plans_trip (email_id, trip_id)
    VALUES (email, trip_id);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_trip` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_trip`(
    IN trip_name VARCHAR(255),
    IN start_date DATE,
    IN end_date DATE,
    IN status ENUM('Planning In Progress','Planned Successfully','Ongoing', 'Completed')
)
BEGIN
    INSERT INTO trip (trip_name, start_date, end_date, trip_status)
    VALUES (trip_name, start_date, end_date, status);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_trip_destination` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_trip_destination`(
     IN dest_id INT,
     IN trip_id INT,
     IN transport_mode TEXT,
     IN travel_dur TIME
 )
BEGIN
     INSERT INTO trip_has_destination (destination_id, trip_id, transportation_mode, travel_duration)
     VALUES (dest_id, trip_id, transport_mode, travel_dur);
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `add_trip_item` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `add_trip_item`(
     IN trip_id INT,
     IN item_id INT
 )
BEGIN
     INSERT INTO trip_requires_item (trip_id, item_id)
     VALUES (trip_id, item_id);
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_activity_by_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_activity_by_id`(IN act_id INT)
BEGIN
    DELETE FROM activity_sightseeing WHERE activity_id = act_id;
    DELETE FROM activity_adventuresport WHERE activity_id = act_id;
    DELETE FROM activity WHERE activity_id = act_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_expense_by_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_expense_by_id`(IN exp_id INT)
BEGIN
     DELETE FROM Expense WHERE expense_id = exp_id;
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_homestay_accommodation_by_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_homestay_accommodation_by_id`(IN accom_id INT)
BEGIN
    DELETE FROM accommodation_homestay WHERE accommodation_id = accom_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_hostel_accommodation_by_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_hostel_accommodation_by_id`(IN accom_id INT)
BEGIN
    DELETE FROM Accommodation_Hostel WHERE accommodation_id = accom_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_hotel_accommodation_by_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_hotel_accommodation_by_id`(IN accom_id INT)
BEGIN
    DELETE FROM accommodation_hotel WHERE accommodation_id = accom_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_trip_by_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_trip_by_id`(IN id INT)
BEGIN
    DELETE FROM trip WHERE trip_id = id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_trip_destination` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_trip_destination`(
    IN dest_id INT,
    IN p_trip_id INT
)
BEGIN
    DELETE FROM Trip_Has_Destination WHERE (destination_id = dest_id AND trip_id = p_trip_id);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `delete_trip_required_item` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_trip_required_item`(
     IN p_trip_id INT,
     IN p_item_id INT
 )
BEGIN
     DELETE FROM trip_requires_item WHERE trip_id = p_trip_id AND item_id = p_item_id;
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_accommodation_choices_by_travel_duration` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_accommodation_choices_by_travel_duration`()
BEGIN
    SELECT
        Accommodation_Hotel.accommodation_name,
        DATEDIFF(Accommodation_Hotel.checkout_date, Accommodation_Hotel.checkin_date) AS duration,
        COUNT(*) AS booking_count
    FROM Accommodation_Hotel
    GROUP BY Accommodation_Hotel.accommodation_name, duration
    ORDER BY duration DESC, booking_count DESC;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_average_activity_cost_by_country` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_average_activity_cost_by_country`()
BEGIN
    SELECT Destination.country, AVG(Activity.cost) AS average_cost
    FROM Activity
    JOIN Destination ON Activity.destination_id = Destination.destination_id
    GROUP BY Destination.country;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_common_packing_items` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_common_packing_items`()
BEGIN
    SELECT essential_packing_item.item_name, COUNT(*) AS item_count
    FROM essential_packing_item
    JOIN Trip_Requires_Item ON essential_packing_item.item_id = Trip_Requires_Item.item_id
    GROUP BY essential_packing_item.item_name
    ORDER BY item_count DESC
    LIMIT 10;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_destination_popularity_over_time` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_destination_popularity_over_time`()
BEGIN
    SELECT destination.destination_name, YEAR(trip.start_date) AS year, MONTH(trip.start_date) AS month,
           COUNT(*) AS visit_count
    FROM destination
    JOIN trip_has_destination ON destination.destination_id = trip_has_destination.destination_id
    JOIN trip ON trip_has_destination.trip_id = trip.trip_id
    WHERE trip.trip_status = 'Completed'
    GROUP BY destination.destination_name, YEAR(trip.start_date), MONTH(trip.start_date)
    ORDER BY destination.destination_name, year, month;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_traveler_trip_counts_and_expenses` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_traveler_trip_counts_and_expenses`()
BEGIN
    SELECT traveller.email_id, traveller.first_name, traveller.last_name,
           COUNT(DISTINCT trip.trip_id) AS total_trips,
           SUM(Expense.amount) AS total_expenses
    FROM traveller
    JOIN traveller_plans_trip ON traveller.email_id = traveller_plans_trip.email_id
    JOIN Trip ON traveller_plans_trip.trip_id = trip.trip_id
    LEFT JOIN expense ON trip.trip_id = expense.trip_id
    GROUP BY traveller.email_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_traveller_by_email` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_traveller_by_email`(IN email VARCHAR(255))
BEGIN
    SELECT * FROM Traveller WHERE email_id = email;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `get_trips_by_traveller_email` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `get_trips_by_traveller_email`(IN email_id VARCHAR(255))
BEGIN
    select * from trip where trip_id in (select trip_id from traveller_plans_trip where
    traveller_plans_trip.email_id=email_id);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_destination` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_destination`(
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_traveller` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_traveller`(IN p_email_id VARCHAR(255), IN p_first_name VARCHAR(100), IN p_last_name VARCHAR(100),
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_trip` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_trip`(
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_trip_has_destination` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_trip_has_destination`(
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
 END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-18 18:27:20
