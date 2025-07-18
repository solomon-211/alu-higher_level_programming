-- Task: Show the structure of first_table without DESCRIBE/EXPLAIN

-- Query to get table structure from information_schema
SELECT 
    COLUMN_NAME, 
    COLUMN_TYPE, 
    IS_NULLABLE, 
    COLUMN_KEY, 
    COLUMN_DEFAULT, 
    EXTRA
FROM 
    information_schema.COLUMNS
WHERE 
    TABLE_SCHEMA = DATABASE()
    AND TABLE_NAME = 'first_table';
