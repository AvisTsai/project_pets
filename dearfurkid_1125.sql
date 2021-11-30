-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: fk_test
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add 標籤',7,'add_tag'),(26,'Can change 標籤',7,'change_tag'),(27,'Can delete 標籤',7,'delete_tag'),(28,'Can view 標籤',7,'view_tag'),(29,'Can add 會員管理',8,'add_membermanagement'),(30,'Can change 會員管理',8,'change_membermanagement'),(31,'Can delete 會員管理',8,'delete_membermanagement'),(32,'Can view 會員管理',8,'view_membermanagement'),(33,'Can add 寵物',9,'add_pet'),(34,'Can change 寵物',9,'change_pet'),(35,'Can delete 寵物',9,'delete_pet'),(36,'Can view 寵物',9,'view_pet'),(37,'Can add 記帳',10,'add_money'),(38,'Can change 記帳',10,'change_money'),(39,'Can delete 記帳',10,'delete_money'),(40,'Can view 記帳',10,'view_money'),(41,'Can add 註冊',11,'add_register'),(42,'Can change 註冊',11,'change_register'),(43,'Can delete 註冊',11,'delete_register'),(44,'Can view 註冊',11,'view_register'),(45,'Can add event',12,'add_event'),(46,'Can change event',12,'change_event'),(47,'Can delete event',12,'delete_event'),(48,'Can view event',12,'view_event'),(49,'Can add category',13,'add_category'),(50,'Can change category',13,'change_category'),(51,'Can delete category',13,'delete_category'),(52,'Can view category',13,'view_category'),(53,'Can add item',14,'add_item'),(54,'Can change item',14,'change_item'),(55,'Can delete item',14,'delete_item'),(56,'Can view item',14,'view_item');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$jllX9ECRppzyEoTmaHBV27$XLC8ENuaUqu07FEgQUl19dN6B1dLeeSHa80tq2YKT0Q=','2021-11-23 08:51:38.828200',1,'admin','','','123@gmail.com',1,1,'2021-11-23 08:51:23.727760');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-11-23 08:51:52.997051','1','toy',1,'[{\"added\": {}}]',10,1),(2,'2021-11-23 08:52:28.516327','2','toy',1,'[{\"added\": {}}]',10,1),(3,'2021-11-23 09:02:17.157507','3','food',1,'[{\"added\": {}}]',10,1),(4,'2021-11-23 09:02:45.804176','4','others',1,'[{\"added\": {}}]',10,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(13,'pets','category'),(12,'pets','event'),(14,'pets','item'),(8,'pets','membermanagement'),(10,'pets','money'),(9,'pets','pet'),(11,'pets','register'),(7,'pets','tag'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-11-21 14:25:33.062135'),(2,'auth','0001_initial','2021-11-21 14:25:35.778897'),(3,'admin','0001_initial','2021-11-21 14:25:36.616256'),(4,'admin','0002_logentry_remove_auto_add','2021-11-21 14:25:36.700586'),(5,'admin','0003_logentry_add_action_flag_choices','2021-11-21 14:25:36.765136'),(6,'contenttypes','0002_remove_content_type_name','2021-11-21 14:25:37.160986'),(7,'auth','0002_alter_permission_name_max_length','2021-11-21 14:25:37.741808'),(8,'auth','0003_alter_user_email_max_length','2021-11-21 14:25:38.193991'),(9,'auth','0004_alter_user_username_opts','2021-11-21 14:25:38.268940'),(10,'auth','0005_alter_user_last_login_null','2021-11-21 14:25:38.629321'),(11,'auth','0006_require_contenttypes_0002','2021-11-21 14:25:38.651961'),(12,'auth','0007_alter_validators_add_error_messages','2021-11-21 14:25:38.738885'),(13,'auth','0008_alter_user_username_max_length','2021-11-21 14:25:39.152912'),(14,'auth','0009_alter_user_last_name_max_length','2021-11-21 14:25:40.047819'),(15,'auth','0010_alter_group_name_max_length','2021-11-21 14:25:40.438916'),(16,'auth','0011_update_proxy_permissions','2021-11-21 14:25:40.529427'),(17,'auth','0012_alter_user_first_name_max_length','2021-11-21 14:25:40.868144'),(18,'pets','0001_initial','2021-11-21 14:25:42.780394'),(19,'pets','0002_auto_20210507_1607','2021-11-21 14:25:43.865736'),(20,'pets','0003_auto_20210529_1848','2021-11-21 14:25:44.028927'),(21,'pets','0004_auto_20210604_1933','2021-11-21 14:25:45.718017'),(22,'pets','0005_delete_register','2021-11-21 14:25:45.870134'),(23,'pets','0006_auto_20210611_1151','2021-11-21 14:25:46.105965'),(24,'pets','0007_auto_20210611_1706','2021-11-21 14:25:46.275104'),(25,'pets','0008_auto_20210611_1747','2021-11-21 14:25:46.641000'),(26,'pets','0009_rename_userid_register_username','2021-11-21 14:25:46.777080'),(27,'pets','0010_alter_register_check_password','2021-11-21 14:25:46.820562'),(28,'pets','0011_alter_money_time','2021-11-21 14:25:46.864845'),(29,'pets','0012_auto_20210716_2110','2021-11-21 14:25:47.093792'),(30,'pets','0013_alter_money_category','2021-11-21 14:25:47.113165'),(31,'pets','0014_auto_20210722_1926','2021-11-21 14:25:47.158290'),(32,'pets','0015_auto_20210722_1929','2021-11-21 14:25:47.205332'),(33,'pets','0016_auto_20210805_2300','2021-11-21 14:25:47.234211'),(34,'pets','0017_alter_money_time','2021-11-21 14:25:47.250170'),(35,'pets','0018_alter_money_time','2021-11-21 14:25:47.269814'),(36,'pets','0019_alter_money_time','2021-11-21 14:25:47.288803'),(37,'pets','0020_alter_money_time','2021-11-21 14:25:47.310229'),(38,'pets','0014_auto_20210801_2043','2021-11-21 14:25:47.332033'),(39,'pets','0021_merge_0014_auto_20210801_2043_0020_alter_money_time','2021-11-21 14:25:47.347230'),(40,'pets','0022_auto_20211015_1607','2021-11-21 14:25:47.492832'),(41,'pets','0023_alter_money_time','2021-11-21 14:25:47.530954'),(42,'pets','0024_auto_20211021_1910','2021-11-21 14:25:47.581275'),(43,'pets','0025_auto_20211030_1312','2021-11-21 14:25:47.641618'),(44,'pets','0026_auto_20211102_2127','2021-11-21 14:25:50.021728'),(45,'pets','0023_alter_event_title','2021-11-21 14:25:50.065130'),(46,'pets','0027_merge_0023_alter_event_title_0026_auto_20211102_2127','2021-11-21 14:25:50.097890'),(47,'sessions','0001_initial','2021-11-21 14:25:50.338037'),(48,'pets','0028_auto_20211118_2316','2021-11-23 06:06:09.599344'),(49,'pets','0029_auto_20211123_1406','2021-11-23 09:01:18.943758'),(50,'pets','0030_alter_money_time','2021-11-23 09:12:56.753677');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('uve26pkylxx6ml2fxni83hwlsgwurwg9','.eJxVjMEKwyAQRP_FcxEVzZoee-83yLquNW1RiMkp9N-bQA7taWDem9lEwHUpYe08hymJq9Di8ttFpBfXA6Qn1keT1OoyT1Eeijxpl_eW-H073b-Dgr3saw_W8ehtYvDWOMo2Zg0wWnaANBiVDGanjEmwhyLPpA0yEA3kIijx-QLV1Tfc:1mpRWc:BNGU5e_M9Mvff-CJPkchqMPGtedOvsWRXMns4jYQyMc','2021-12-07 08:51:38.863228');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets_event`
--

DROP TABLE IF EXISTS `pets_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets_event` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  `start_time` date NOT NULL,
  `end_time` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets_event`
--

LOCK TABLES `pets_event` WRITE;
/*!40000 ALTER TABLE `pets_event` DISABLE KEYS */;
INSERT INTO `pets_event` VALUES (1,'dance','dance sing','2021-12-01','2021-12-01'),(3,'go to park','park&store','2021-11-30','2021-12-01'),(4,'dance','dance','2021-11-09','2021-11-09'),(5,'visit the friend','SSS','2021-11-30','2021-11-30'),(6,'train','train','2021-11-19','2021-11-19');
/*!40000 ALTER TABLE `pets_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets_membermanagement`
--

DROP TABLE IF EXISTS `pets_membermanagement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets_membermanagement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `UserID` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `UserName` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `UserAccount` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `UserPassword` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Email` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UserID` (`UserID`),
  UNIQUE KEY `UserName` (`UserName`),
  UNIQUE KEY `UserAccount` (`UserAccount`),
  UNIQUE KEY `UserPassword` (`UserPassword`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets_membermanagement`
--

LOCK TABLES `pets_membermanagement` WRITE;
/*!40000 ALTER TABLE `pets_membermanagement` DISABLE KEYS */;
/*!40000 ALTER TABLE `pets_membermanagement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets_money`
--

DROP TABLE IF EXISTS `pets_money`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets_money` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `time` datetime(6) NOT NULL,
  `item` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `price` int NOT NULL,
  `category` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets_money`
--

LOCK TABLES `pets_money` WRITE;
/*!40000 ALTER TABLE `pets_money` DISABLE KEYS */;
INSERT INTO `pets_money` VALUES (1,'2021-11-17 00:00:00.000000','toy',213,'toy'),(2,'2021-11-23 00:00:00.000000','toy',9,'toy'),(3,'2021-11-01 00:00:00.000000','food',90,'food'),(4,'2021-11-02 00:00:00.000000','others',30,'others');
/*!40000 ALTER TABLE `pets_money` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets_pet`
--

DROP TABLE IF EXISTS `pets_pet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets_pet` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `description` longtext COLLATE utf8_unicode_ci NOT NULL,
  `species` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `gender` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets_pet`
--

LOCK TABLES `pets_pet` WRITE;
/*!40000 ALTER TABLE `pets_pet` DISABLE KEYS */;
/*!40000 ALTER TABLE `pets_pet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets_register`
--

DROP TABLE IF EXISTS `pets_register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets_register` (
  `id` char(32) COLLATE utf8_unicode_ci NOT NULL,
  `user_pwd` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `username` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `user_email` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `check_password` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets_register`
--

LOCK TABLES `pets_register` WRITE;
/*!40000 ALTER TABLE `pets_register` DISABLE KEYS */;
INSERT INTO `pets_register` VALUES ('0d049bd459934d2db54947bcb5005e24','1234','1234','1234@gmail.com','1234'),('765f504a512045da9a4cb0f6fa7a0b28','happy','happy','123@gmail.com','happy'),('84f52cbada504375a03f5657df876026','123','123','123@gmail.com','`12'),('b7e24a90715549939861b2ac4543bc31','123','123','123@gmail.com','123'),('c7ee8102ce214fcfa61f454554a0c4c9','abcd','abcd','ABCD@gmail.com','BCD');
/*!40000 ALTER TABLE `pets_register` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pets_tag`
--

DROP TABLE IF EXISTS `pets_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pets_tag` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pets_tag`
--

LOCK TABLES `pets_tag` WRITE;
/*!40000 ALTER TABLE `pets_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `pets_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'fk_test'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-25 16:48:19
