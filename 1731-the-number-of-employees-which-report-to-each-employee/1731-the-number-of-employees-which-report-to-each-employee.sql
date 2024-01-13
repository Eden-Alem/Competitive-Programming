# Write your MySQL query statement below

SELECT e.employee_id, e.name, r.reports_count, r.average_age
FROM employees e INNER JOIN (
        SELECT reports_to, COUNT(reports_to) AS reports_count, ROUND(AVG(age)) AS average_age
        FROM employees
        WHERE reports_to IS NOT NULL
        GROUP BY reports_to
    ) r
ON r.reports_to = e.employee_id
ORDER BY e.employee_id
