# Write your MySQL query statement below
SELECT e1.name
FROM employee e1 JOIN employee e2
ON e1.id = e2.managerId
GROUP BY e1.id
HAVING COUNT(e2.managerId) >= 5;
