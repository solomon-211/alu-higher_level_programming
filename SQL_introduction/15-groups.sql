-- Task: Count records by score in second_table

-- Query to group records by score and count occurrences
SELECT 
    score,
    COUNT(*) AS number
FROM 
    second_table
GROUP BY 
    score
ORDER BY 
    number DESC;
