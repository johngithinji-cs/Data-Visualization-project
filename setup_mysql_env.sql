-- Script to prepare a MySQL server for the project
-- Setup development

CREATE DATABASE IF NOT EXISTS user_data;
CREATE USER IF NOT EXISTS 'analyst'@'localhost' IDENTIFIED BY 'project';
GRANT ALL ON  user_data.* TO 'analyst'@'localhost';
GRANT SELECT ON performance_schema.* TO 'analyst'@'localhost';
