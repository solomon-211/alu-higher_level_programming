-- Script to print full description of first_table from hbtn_0c_0 database
-- Usage: mysql -u username -p hbtn_0c_0 < script_name.sql

SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM 
    INFORMATION_SCHEMA.COLUMNS 
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' 
    AND TABLE_NAME = 'first_table'
ORDER BY 
    ORDINAL_POSITION;
