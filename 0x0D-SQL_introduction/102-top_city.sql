-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT city, AVG(temp) AS avg_temp
FROM val
WHERE month = 7 OR month = 8 
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
