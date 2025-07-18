-- Script to list all records from second_table ordered by score (top first)
-- Usage: mysql -u username -p hbtn_0c_0 < script_name.sql

SELECT score, name FROM second_table ORDER BY score DESC;
