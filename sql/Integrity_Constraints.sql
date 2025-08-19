-- create referential integrity constraints for the lunches database
alter table employees
add constraint fk_employees_dept_code
foreign key (dept_code)
   references departments (dept_code);


alter table employees
add constraint fk_employees_manager_id
foreign key (manager_id)
   references employees (employee_id);


alter table lunches
add constraint fk_lunches_employees
foreign key (employee_id)
   references employees (employee_id);


alter table lunch_items
add constraint fk_lunch_items_lunches
foreign key (lunch_id)
   references lunches (lunch_id);


alter table lunch_items
add constraint fk_lunch_items_foods
foreign key (supplier_id, product_code)
   references foods (supplier_id, product_code);


alter table foods
add constraint fk_foods_suppliers
foreign key (supplier_id)
   references suppliers (supplier_id)
   on delete cascade;



-- create not null constraints - make a required field
alter table employees
add constraint nn_employees_first_name
   check (first_name is not null);


alter table employees
add constraint nn_employees_last_name
   check (last_name is not null);


alter table lunches
add constraint nn_lunches_employee_id
check (employee_id is not null);


-- create uniqueness constraints
alter table employees
add constraint unique_employees_fulname
   unique (first_name, last_name);


alter table employees
add constraint unique_empployees_phone_num
   unique (phone_number);


-- create check constraints
alter table foods
add constraint check_foods_price_max_price
check (price < 10.00);

