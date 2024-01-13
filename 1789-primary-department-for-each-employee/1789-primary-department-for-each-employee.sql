# Write your MySQL query statement below

SELECT employee_id, 
    (CASE WHEN COUNT(department_id) = 1 THEN department_id
         WHEN COUNT(department_id) > 1 THEN SUM((primary_flag='Y')*department_id)
    END) AS department_id
FROM employee
GROUP BY employee_id
HAVING ((COUNT(department_id) > 1) AND (SUM((primary_flag='Y')*department_id) != 0))
    OR ((COUNT(department_id) = 1));