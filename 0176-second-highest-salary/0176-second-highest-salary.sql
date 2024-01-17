# Write your MySQL query statement below

SELECT (SELECT DISTINCT Salary AS SecondHighestSalary
FROM (
    SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS rank_
    FROM employee
) ranked
WHERE rank_ = 2) AS SecondHighestSalary
