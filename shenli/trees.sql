-- --------------------------------------------------------
-- 主机:                           localhost
-- 服务器版本:                        8.0.27 - MySQL Community Server - GPL
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  8.2.0.4675
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 trees 的数据库结构
CREATE DATABASE IF NOT EXISTS `trees` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `trees`;


-- 导出  表 trees.conflagration 结构
CREATE TABLE IF NOT EXISTS `conflagration` (
  `year` int NOT NULL COMMENT '年份',
  `commonly` int NOT NULL COMMENT '一般火灾次数(次)',
  `more` int NOT NULL COMMENT '较大火灾次数(次)',
  `major` int NOT NULL COMMENT '重大火灾次数(次)',
  `significant` int NOT NULL COMMENT '特别重大火灾次数(次)',
  PRIMARY KEY (`year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='森林火灾次数';

-- 正在导出表  trees.conflagration 的数据：~17 rows (大约)
/*!40000 ALTER TABLE `conflagration` DISABLE KEYS */;
INSERT INTO `conflagration` (`year`, `commonly`, `more`, `major`, `significant`) VALUES
	(2004, 6531, 0, 38, 3),
	(2005, 4949, 0, 16, 3),
	(2006, 2691, 0, 7, 5),
	(2007, 3205, 0, 4, 0),
	(2008, 5673, 0, 13, 0),
	(2009, 4945, 3878, 35, 1),
	(2010, 4795, 2902, 22, 4),
	(2011, 2993, 2548, 9, 0),
	(2012, 2397, 1568, 1, 0),
	(2013, 2347, 1582, 0, 0),
	(2014, 2080, 1620, 2, 1),
	(2015, 1676, 1254, 6, 0),
	(2016, 1340, 693, 1, 0),
	(2017, 2258, 958, 4, 3),
	(2018, 1579, 894, 3, 2),
	(2019, 1534, 802, 8, 1),
	(2020, 722, 424, 7, 0);
/*!40000 ALTER TABLE `conflagration` ENABLE KEYS */;


-- 导出  表 trees.forest 结构
CREATE TABLE IF NOT EXISTS `forest` (
  `year` int DEFAULT NULL COMMENT '年份',
  `forestrylandarea` double DEFAULT NULL COMMENT '林业用地面积(万公顷)',
  `forestcoverage` double DEFAULT NULL COMMENT '森林面积(万公顷)',
  `plantationarea` double DEFAULT NULL COMMENT '人工林面积(万公顷)',
  `forest` double DEFAULT NULL COMMENT '森林覆盖率(%)',
  `livingtree` double DEFAULT NULL COMMENT '活立木总蓄积量(亿立方米)',
  `standingtree` double DEFAULT NULL COMMENT '森林蓄积量(亿立方米)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COMMENT='森林';

-- 正在导出表  trees.forest 的数据：~17 rows (大约)
/*!40000 ALTER TABLE `forest` DISABLE KEYS */;
INSERT INTO `forest` (`year`, `forestrylandarea`, `forestcoverage`, `plantationarea`, `forest`, `livingtree`, `standingtree`) VALUES
	(2004, 30590.41, 19545.22, 6168.84, 20.4, 149.13, 137.21),
	(2005, 30590.41, 19545.22, 6168.84, 20.4, 149.13, 137.21),
	(2006, 30590.41, 19545.22, 6168.84, 20.4, 149.13, 137.21),
	(2007, 30590.41, 19545.22, 6168.84, 20.4, 149.13, 137.21),
	(2008, 30590.41, 19545.22, 6168.84, 20.4, 149.13, 137.21),
	(2009, 31259, 20768.73, 6933.38, 21.6, 164.33, 151.37),
	(2010, 31259, 20768.73, 6933.38, 21.6, 164.33, 151.37),
	(2011, 31259, 20768.73, 6933.38, 21.6, 164.33, 151.37),
	(2012, 31259, 20768.73, 6933.38, 21.6, 164.33, 151.37),
	(2013, 31259, 20768.73, 6933.38, 21.6, 164.33, 151.37),
	(2014, 32368.55, 22044.62, 8003.1, 23, 190.07, 175.6),
	(2015, 32368.55, 22044.62, 8003.1, 23, 190.07, 175.6),
	(2016, 32368.55, 22044.62, 8003.1, 23, 190.07, 175.6),
	(2017, 32368.55, 22044.62, 8003.1, 23, 190.07, 175.6),
	(2018, 32368.55, 22044.62, 8003.1, 23, 190.07, 175.6),
	(2019, 32368.55, 22044.62, 8003.1, 23, 190.07, 175.6),
	(2020, 32368.55, 22044.62, 8003.1, 23, 190.07, 175.6);
/*!40000 ALTER TABLE `forest` ENABLE KEYS */;


-- 导出  表 trees.user 结构
CREATE TABLE IF NOT EXISTS `user` (
  `id` varchar(50) DEFAULT NULL,
  `password` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- 正在导出表  trees.user 的数据：~4 rows (大约)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` (`id`, `password`) VALUES
	('admin', 123),
	('ma', 564),
	('as', 22),
	('cvc', 256),
	('aaaaaa', 123456);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
