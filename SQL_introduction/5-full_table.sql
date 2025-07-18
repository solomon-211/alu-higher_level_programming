-- Task: Show the complete CREATE TABLE statement for first_table

-- Query to get the full table creation syntax
SELECT 
    TABLE_NAME,
    CREATE_TABLE
FROM 
    information_schema.TABLES
WHERE 
    TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'first_table'\G
