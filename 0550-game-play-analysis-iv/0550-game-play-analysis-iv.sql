# Write your MySQL query statement below
WITH CTE AS
(
    SELECT player_id, MIN(event_date) as first_date
    FROM activity
    GROUP BY player_id
)

SELECT ROUND(SUM(IF(DATEDIFF(a.event_date, c.first_date) = 1,1,0))/COUNT(DISTINCT a.player_id), 2) AS fraction
FROM activity a LEFT JOIN CTE c
ON a.player_id = c.player_id
