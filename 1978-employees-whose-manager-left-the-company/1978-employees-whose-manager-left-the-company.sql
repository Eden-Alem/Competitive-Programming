# Write your MySQL query statement below

WITH cte AS
(SELECT employee_id, manager_id
FROM employees
WHERE salary < 30000)

SELECT employee_id
FROM cte
WHERE manager_id NOT IN (SELECT employee_id 
                        FROM employees)
ORDER BY employee_id