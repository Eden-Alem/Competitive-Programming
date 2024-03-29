# Write your MySQL query statement below

SELECT machine_id, 
ROUND((SUM(CASE WHEN activity_type = 'end' THEN timestamp ELSE timestamp * -1 END)) / (SELECT COUNT(DISTINCT process_id)), 3) AS processing_time
FROM Activity
GROUP BY machine_id
