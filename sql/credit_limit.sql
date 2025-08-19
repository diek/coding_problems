SELECT employee_id,
	   last_name,
	   credit_limit
FROM employees
WHERE credit_limit > 20.00
ORDER BY last_name;