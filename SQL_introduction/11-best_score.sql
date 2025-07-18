-- Script to list records with score >= 10 from second_table ordered by score (top first)
-- Usage: mysql -u username -p hbtn_0c_0 < script_name.sql

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
