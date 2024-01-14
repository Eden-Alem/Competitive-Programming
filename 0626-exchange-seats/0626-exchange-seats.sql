# Write your MySQL query statement below

SELECT id, ifnull((CASE
                WHEN id % 2 = 0 THEN lag_student ELSE lead_student END), student) 
                AS student
FROM
(SELECT id, student, LAG(student) OVER (ORDER BY ID) lag_student, LEAD(student) OVER (ORDER BY ID) lead_student 
FROM seat) AS lag_lead_student