-- 
-- This SQL script creates the Airline database's tables
--

--
-- Table structure for table `aircraft`
--

DROP TABLE IF EXISTS `aircraft`;
CREATE TABLE `aircraft` (
  `AircraftType` char(3) NOT NULL,
  `AircraftDescription` varchar(32) NOT NULL,
  `SeatingCapacity` decimal(3,0) DEFAULT NULL,
  PRIMARY KEY (`AircraftType`)
);

--
-- Dumping data for table `aircraft`
--

INSERT INTO `aircraft` VALUES ('727','Boeing 727',150),('737','Boeing 737',120),('743','Boeing 747-338',420),('744','Boeing 747-438',420),('74L','Boeing 747SP',260),('757','Boeing 757',150),('767','Boeing 767',260),('AB3','Airbus A300',250),('D10','McDonnel Douglas DC10',150);

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
CREATE TABLE `cities` (
  `CityCode` char(3) NOT NULL,
  `CityName` varchar(24) NOT NULL,
  `CountryCode` char(3) NOT NULL,
  PRIMARY KEY (`CityCode`)
);

--
-- Dumping data for table `cities`
--

INSERT INTO `cities` VALUES ('ADL','Adelaide','AUS'),('AKL','Auckland','NZL'),('BNE','Brisbane','AUS'),('BRI','Brisbane','USA'),('CBR','Canberra','AUS'),('CGK','Jakarta','IND'),('HNL','Honolulu','USA'),('LAX','Los Angeles','USA'),('MEL','Melbourne','AUS'),('SFO','San Francisco','USA'),('SYD','Sydney','AUS');

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
CREATE TABLE `countries` (
  `CountryCode` char(3) NOT NULL,
  `CountryName` varchar(32) NOT NULL,
  PRIMARY KEY (`CountryCode`)
);

--
-- Dumping data for table `countries`
--

INSERT INTO `countries` VALUES ('AUS','Australia'),('IND','Indonesia'),('MLY','Malaysia'),('NZL','New Zealand'),('USA','United States of America');

--
-- Table structure for table `flights`
--

DROP TABLE IF EXISTS `flights`;
CREATE TABLE `flights` (
  `FlightNum` decimal(2,0) NOT NULL,
  `FromCityCode` char(3) NOT NULL,
  `ToCityCode` char(3) NOT NULL,
  `SeatsRemaining` decimal(3,0) DEFAULT NULL,
  `AircraftType` char(3) DEFAULT NULL,
  PRIMARY KEY (`FlightNum`)
);

--
-- Dumping data for table `flights`
--

INSERT INTO `flights` VALUES (1,'BNE','SYD',10,'AB3'),(2,'SYD','CBR',20,'727'),(3,'SYD','MEL',30,'757'),(4,'SYD','AKL',40,'D10'),(5,'BNE','CGK',50,'757'),(6,'BNE','LAX',60,'74L'),(7,'SYD','HNL',70,'767'),(8,'HNL','SFO',80,'767'),(9,'SYD','LAX',90,'744'),(10,'SYD','BNE',100,'AB3');

-- Dump completed on 2011-09-12 16:50:00
