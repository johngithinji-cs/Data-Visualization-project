-- Script to prepare a MySQL server for the project
-- Setup development

CREATE DATABASE IF NOT EXISTS user_csv_files;
CREATE USER IF NOT EXISTS 'analyst'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON  user_csv_files.* TO 'analyst'@'localhost';
GRANT SELECT ON performance_schema.* TO 'analyst'@'localhost';
