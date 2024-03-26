-- lists all records of the table
SELECT score, name
FROM second_late
WHERE name != ''
ORDER BY score DESC;
