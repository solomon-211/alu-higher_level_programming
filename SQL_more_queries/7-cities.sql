-- Creates database hbtn_0d_usa and table cities with proper constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- First ensure the states table exists (required for foreign key)
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id)
);

-- Create the cities table with foreign key constraint
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
