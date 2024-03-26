-- a script that lists all records of the table second_table sorted by score with first column as score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
