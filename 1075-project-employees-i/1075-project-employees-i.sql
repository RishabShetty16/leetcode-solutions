SELECT pr.project_id, ROUND(AVG(e.experience_years),2) as average_years
FROM Project pr 
JOIN Employee e 
ON pr.employee_id = e.employee_id
GROUP BY pr.project_id; 