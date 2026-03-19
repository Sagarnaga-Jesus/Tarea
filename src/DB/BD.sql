-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.31 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.15.0.7171
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para registro
CREATE DATABASE IF NOT EXISTS `registro` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `registro`;

-- Volcando estructura para tabla registro.tareas
CREATE TABLE IF NOT EXISTS `tareas` (
  `id_tarea` int DEFAULT NULL,
  `id_usuario` int DEFAULT '0',
  `titulo` varchar(200) DEFAULT NULL,
  `desripcion` text,
  `fecha_creacion` timestamp NULL DEFAULT NULL,
  `feha_limite` date DEFAULT '0000-00-00',
  `hora_limite` time DEFAULT '00:00:00'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla registro.tareas: 0 rows
/*!40000 ALTER TABLE `tareas` DISABLE KEYS */;
/*!40000 ALTER TABLE `tareas` ENABLE KEYS */;

-- Volcando estructura para tabla registro.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id_usuario` int DEFAULT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `contraseña` varchar(300) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `fecha_registro` timestamp NULL DEFAULT NULL,
  `ultimo_ingreso` timestamp NULL DEFAULT NULL,
  `activo` tinyint DEFAULT NULL,
  `foto` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla registro.usuario: 1 rows
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` (`id_usuario`, `nombre`, `apellido`, `email`, `contraseña`, `telefono`, `fecha_registro`, `ultimo_ingreso`, `activo`, `foto`) VALUES
	(NULL, 'Admin', 'Admins', 'Admin@gmail.com', 'Admin#19', '6562321212', '2026-03-19 11:24:00', '2026-03-19 11:24:02', 1, NULL);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
