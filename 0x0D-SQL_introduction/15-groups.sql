--  lists the number of records with the same score
SELECT count(score) AS number
FROM second_table
ORDER BY number DESC;
