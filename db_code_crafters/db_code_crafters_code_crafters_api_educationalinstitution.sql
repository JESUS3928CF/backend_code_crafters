CREATE DATABASE  IF NOT EXISTS `db_code_crafters` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_code_crafters`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: db_code_crafters
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `code_crafters_api_educationalinstitution`
--

DROP TABLE IF EXISTS `code_crafters_api_educationalinstitution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `code_crafters_api_educationalinstitution` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `web_site` varchar(200) NOT NULL,
  `id_support_id` bigint NOT NULL,
  `id_type_institute_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `code_crafters_api_ed_id_support_id_f043d45b_fk_code_craf` (`id_support_id`),
  KEY `code_crafters_api_ed_id_type_institute_id_b24c612f_fk_code_craf` (`id_type_institute_id`),
  CONSTRAINT `code_crafters_api_ed_id_support_id_f043d45b_fk_code_craf` FOREIGN KEY (`id_support_id`) REFERENCES `code_crafters_api_support` (`id`),
  CONSTRAINT `code_crafters_api_ed_id_type_institute_id_b24c612f_fk_code_craf` FOREIGN KEY (`id_type_institute_id`) REFERENCES `code_crafters_api_typeinstitute` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `code_crafters_api_educationalinstitution`
--

LOCK TABLES `code_crafters_api_educationalinstitution` WRITE;
/*!40000 ALTER TABLE `code_crafters_api_educationalinstitution` DISABLE KEYS */;
/*!40000 ALTER TABLE `code_crafters_api_educationalinstitution` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-27 15:08:22
