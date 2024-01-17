# Write your MySQL query statement below

SELECT MAX(Salary) AS SecondHighestSalary
FROM employee
WHERE Salary < (SELECT MAX(Salary) FROM employee)
