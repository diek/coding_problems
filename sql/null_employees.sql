SELECT employee_id,
       first_name,
       last_name,
       manager_id
from employees
where manager_id is null;
