-- MySQL dump 10.13  Distrib 8.0.23, for macos10.15 (x86_64)
--
-- Host: localhost    Database: db_share_location
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `Key`
--

DROP TABLE IF EXISTS `Key`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Key` (
  `userId1` int NOT NULL,
  `userId2` int NOT NULL,
  `commonKey` varchar(12) NOT NULL,
  PRIMARY KEY (`userId1`,`userId2`),
  UNIQUE KEY `commonKey_UNIQUE` (`commonKey`),
  KEY `fk_user_key_1_idx` (`userId1`),
  KEY `fk_user_key_2_idx` (`userId2`),
  CONSTRAINT `fk_user_key_1` FOREIGN KEY (`userId1`) REFERENCES `User` (`userId`),
  CONSTRAINT `fk_user_key_2` FOREIGN KEY (`userId2`) REFERENCES `User` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Key`
--

LOCK TABLES `Key` WRITE;
/*!40000 ALTER TABLE `Key` DISABLE KEYS */;
INSERT INTO `Key` VALUES (5,7,'1039112504'),(4,5,'1082382449'),(2,7,'1241932902'),(4,7,'1486773586'),(3,6,'1629529122'),(3,4,'1754518522'),(1,3,'1773916804'),(2,4,'1936376279'),(4,6,'1950397776'),(1,7,'2050623727'),(1,5,'2399362803'),(3,5,'2490631576'),(2,3,'2978157398'),(2,5,'3074149083'),(2,6,'3094724058'),(1,4,'3255482402'),(3,7,'3470120809'),(1,2,'3501381670'),(1,6,'3631806077'),(6,7,'3763443083'),(5,6,'3936345389');
/*!40000 ALTER TABLE `Key` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `userId` int NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `fullName` varchar(45) NOT NULL,
  `avatarUrl` varchar(45) DEFAULT NULL,
  `gender` int NOT NULL,
  `age` int DEFAULT NULL,
  `currentCity` varchar(45) NOT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'sonmt','123456','Mai Truong Son',NULL,0,21,'Haiphong'),(2,'huydq','123456','Dang Quang Huy',NULL,0,21,'Hungyen'),(3,'duongdt','123456','Dao Tung Duong',NULL,0,21,'Haiduong'),(4,'bot1','123456','Bot 1',NULL,1,19,'Haiphong'),(5,'bot2','123456','Bot 2',NULL,1,18,'Hungyen'),(6,'bot3','123456','Bot 3',NULL,0,32,'Haiduong'),(7,'bot4','123456','Bot 4',NULL,2,20,'Ha Noi');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-20 23:57:58
