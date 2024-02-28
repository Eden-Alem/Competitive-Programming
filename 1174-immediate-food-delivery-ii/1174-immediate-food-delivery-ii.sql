# Write your MySQL query statement below
WITH CTE AS (
SELECT customer_id, MIN(order_date) AS min_order_date
FROM delivery
GROUP BY customer_id
)

SELECT ROUND(AVG(IF(d.customer_pref_delivery_date = c.min_order_date, 1, 0)) * 100, 2) AS immediate_percentage
FROM CTE c JOIN delivery d
ON c.customer_id = d.customer_id AND c.min_order_date = d.order_date;