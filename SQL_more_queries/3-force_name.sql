-- Creates table force_name with id and non-null name columns
-- Database name is passed as argument to mysql command
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
