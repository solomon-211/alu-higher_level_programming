-- Script to compute the score average of all records in second_table
-- Usage: mysql -u username -p hbtn_0c_0 < script_name.sql

SELECT AVG(score) AS average FROM second_table;
