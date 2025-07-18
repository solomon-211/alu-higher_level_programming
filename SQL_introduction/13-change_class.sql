-- Script to remove all records with score <= 5 from second_table
-- Usage: mysql -u username -p hbtn_0c_0 < script_name.sql

DELETE FROM second_table WHERE score <= 5;
