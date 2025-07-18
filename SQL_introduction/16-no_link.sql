-- Task: List records from second_table with names, ordered by score

-- Query to select score and name where name is not null
SELECT 
    score, 
    name
FROM 
    second_table
WHERE 
    name IS NOT NULL
ORDER BY 
    score DESC;
