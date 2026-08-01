SELECT e.name 
FROM Employee e
JOIN Employee ee
ON e.id = ee.managerId
GROUP BY ee.managerId 
HAVING COUNT(ee.managerId) >=5