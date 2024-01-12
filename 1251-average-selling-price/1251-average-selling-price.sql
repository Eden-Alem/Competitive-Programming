# Write your MySQL query statement below

SELECT p.product_id, ROUND(COALESCE(SUM(units*price) / SUM(units), 0), 2) AS average_price
FROM prices p LEFT JOIN unitssold u
ON (p.product_id = u.product_id) AND (purchase_date BETWEEN start_date AND end_date)
GROUP BY p.product_id;