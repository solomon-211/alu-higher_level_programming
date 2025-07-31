-- Creates table id_not_null with default id value of 1
-- Database name is passed as argument to mysql command
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
