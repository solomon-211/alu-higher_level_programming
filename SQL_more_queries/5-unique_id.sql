-- Creates table unique_id with unique id column (default 1)
-- Database name is passed as argument to mysql command
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
