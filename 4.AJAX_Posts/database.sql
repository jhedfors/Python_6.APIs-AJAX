-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema posts
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema posts
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `posts` DEFAULT CHARACTER SET utf8 ;
USE `posts` ;

-- -----------------------------------------------------
-- Table `posts`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `posts`.`posts` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `post` TEXT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
