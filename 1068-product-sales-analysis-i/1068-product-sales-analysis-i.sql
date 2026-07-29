SELECT pr.product_name, sa.year, sa.price 
FROM Sales AS sa
JOIN Product AS pr
ON sa.product_id = pr.product_id