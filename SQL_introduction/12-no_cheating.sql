-- Script to update Bob's score to 10 in second_table
-- Usage: mysql -u username -p hbtn_0c_0 < script_name.sql

UPDATE second_table SET score = 10 WHERE name = 'Bob';
