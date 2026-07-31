SELECT pr.product_id, 
    ROUND(IFNULL(SUM(u.units*pr.price)/ SUM(u.units), 0),2) AS average_price
FROM Prices pr
LEFT JOIN UnitsSold u
ON pr.product_id = u.product_id
AND u.purchase_date BETWEEN pr.start_date AND pr.end_date
GROUP BY pr.product_id;