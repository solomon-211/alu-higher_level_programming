-- Task: Show the complete CREATE TABLE statement for first_table

-- Query to get the full table creation syntax
SELECT CONCAT(
    TABLE_NAME,
    'CREATE TABLE `',
    TABLE_NAME,
    '`(\n',
    GROUP_CONCAT(
        '`', COLUMN_NAME, '` ', COLUMN_TYPE,
        IF(IS_NULLABLE = 'NO', ' NOT NULL', ''),
        IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', QUOTE(COLUMN_DEFAULT)), ''),
        IF(EXTRA = 'auto_increment', ' AUTO_INCREMENT', ''),
        IF(COLUMN_KEY = 'PRI', ' PRIMARY KEY', '')
        ORDER BY ORDINAL_POSITION
        SEPARATOR ',\n'
    ),
    '\n) ENGINE=', ENGINE,
    ' DEFAULT CHARSET=', CHARACTER_SET_NAME,
    ' COLLATE=', TABLE_COLLATION
) AS Table_Definition
FROM information_schema.TABLES t
JOIN information_schema.COLUMNS c
    ON t.TABLE_SCHEMA = c.TABLE_SCHEMA
    AND t.TABLE_NAME = c.TABLE_NAME
WHERE t.TABLE_SCHEMA = DATABASE()
    AND t.TABLE_NAME = 'first_table'
GROUP BY t.TABLE_NAME, t.ENGINE, t.CHARACTER_SET_NAME, t.TABLE_COLLATION;
