CREATE DATABASE  IF NOT EXISTS `db_share_location` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_share_location`;
-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: db_share_location
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `commonkey`
--

DROP TABLE IF EXISTS `commonkey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `commonkey` (
  `userId1` int NOT NULL,
  `userId2` int NOT NULL,
  `commonKey` varchar(12) NOT NULL,
  UNIQUE KEY `commonKey_UNIQUE` (`commonKey`),
  KEY `fk_user_key_1_idx` (`userId1`),
  KEY `fk_user_key_2_idx` (`userId2`),
  CONSTRAINT `fk_user_key_1` FOREIGN KEY (`userId1`) REFERENCES `user` (`userId`),
  CONSTRAINT `fk_user_key_2` FOREIGN KEY (`userId2`) REFERENCES `user` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commonkey`
--

LOCK TABLES `commonkey` WRITE;
/*!40000 ALTER TABLE `commonkey` DISABLE KEYS */;
INSERT INTO `commonkey` VALUES (5,7,'1039112504'),(25,26,'1055099045'),(4,5,'1082382449'),(7,27,'1095759248'),(6,25,'1207065641'),(2,7,'1241932902'),(5,28,'1295860251'),(25,27,'1340177055'),(5,27,'1348071515'),(4,25,'1403381219'),(1,25,'1461934068'),(4,7,'1486773586'),(2,27,'1577533312'),(5,26,'1586982553'),(3,6,'1629529122'),(15,26,'1630126552'),(6,27,'1690090003'),(3,4,'1754518522'),(1,3,'1773916804'),(15,25,'1795284242'),(6,26,'1831300047'),(5,25,'1869536126'),(2,4,'1936376279'),(4,6,'1950397776'),(1,26,'2037523472'),(1,7,'2050623727'),(25,28,'2104084077'),(26,28,'2253913050'),(7,28,'2310670719'),(1,5,'2399362803'),(6,28,'2483138939'),(3,5,'2490631576'),(4,27,'2629235581'),(2,25,'2641538931'),(2,28,'2681651885'),(4,28,'2718915004'),(1,27,'2837057400'),(3,27,'2851577574'),(15,27,'2868324551'),(7,25,'2889747941'),(15,28,'2915488200'),(3,28,'2930656111'),(2,3,'2978157398'),(26,27,'3017652654'),(2,5,'3074149083'),(7,26,'3076321443'),(2,6,'3094724058'),(3,25,'3098491445'),(1,4,'3255482402'),(1,28,'3403704154'),(27,28,'3429791158'),(3,7,'3470120809'),(1,2,'3501381670'),(3,26,'3609666369'),(1,6,'3631806077'),(6,7,'3763443083'),(4,26,'3824639565'),(2,26,'3845156926'),(5,6,'3936345389');
/*!40000 ALTER TABLE `commonkey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(64) NOT NULL,
  `fullName` varchar(45) NOT NULL,
  `avatarUrl` varchar(45) DEFAULT NULL,
  `gender` int NOT NULL,
  `birthYear` int DEFAULT NULL,
  `currentCity` varchar(45) NOT NULL,
  `counter` int NOT NULL,
  PRIMARY KEY (`userId`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'sonmt','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','Mai Truong Son',NULL,0,2000,'3',16),(2,'huydq','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','Dang Quang Huy',NULL,0,1999,'3',20),(3,'duongdt','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','Dao Tung Duong',NULL,0,1999,'3',17),(4,'bot1','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','Bot 1',NULL,1,2001,'3',17),(5,'bot2','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','Bot 2',NULL,1,2002,'3',15),(6,'bot3','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','Bot 3',NULL,0,1990,'3',17),(7,'bot4','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','Bot 4',NULL,2,2000,'3',17),(15,'bot5','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','Bot 5',NULL,1,1999,'3',14),(25,'huy11111','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','2','ava.png',0,2000,'3',17),(26,'ab1','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','huyyy','ava.png',0,2000,'3',17),(27,'huy123','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','a','ava.png',0,2000,'3',5),(28,'huy2','fb8e20fc2e4c3f248c60c39bd652f3c1347298bb977b8b4d5903b85055620603','Đặng Quang Huy','ava.png',2,2000,'3',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'db_share_location'
--

--
-- Dumping routines for database 'db_share_location'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-27 15:26:40
