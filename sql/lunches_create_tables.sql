-- EMPLOYEES TABLE
CREATE TABLE employees (
    employee_id    INTEGER PRIMARY KEY,
    first_name     VARCHAR(10) NOT NULL,
    last_name      VARCHAR(20) NOT NULL,
    dept_code      VARCHAR(3),
    hire_date      DATE,
    credit_limit   NUMERIC(4,2),
    phone_number   VARCHAR(4) UNIQUE,
    manager_id     INTEGER,
    CONSTRAINT unique_employees_fullname UNIQUE (first_name, last_name)
);

-- Sequence for EMPLOYEE_ID
CREATE SEQUENCE seq_employee_id
    START 211
    INCREMENT 1;

-- FOODS TABLE
CREATE TABLE foods (
    supplier_id     VARCHAR(3),
    product_code    VARCHAR(2),
    menu_item       INTEGER,
    description     VARCHAR(20),
    price           NUMERIC(4,2),
    price_increase  NUMERIC(4,2),
    CONSTRAINT pk_foods PRIMARY KEY (supplier_id, product_code),
    CONSTRAINT check_foods_price_max_price CHECK (price < 10.00)
);

-- Sequence for MENU_ITEM
CREATE SEQUENCE SEQ_MENU_ITEM
    START 11
    INCREMENT 1;

-- DEPARTMENTS TABLE
CREATE TABLE departments (
    dept_code        VARCHAR(3) PRIMARY KEY,
    department_name  VARCHAR(30)
);

-- LUNCHES TABLE
CREATE TABLE lunches (
    lunch_id      INTEGER PRIMARY KEY,
    lunch_date    DATE,
    employee_id   INTEGER NOT NULL,
    date_entered  DATE
);

-- LUNCH_ITEMS TABLE
CREATE TABLE lunch_items (
    lunch_id       INTEGER,
    item_number    INTEGER,
    supplier_id    VARCHAR(3),
    product_code   VARCHAR(2),
    quantity       INTEGER,
    CONSTRAINT pk_lunch_items PRIMARY KEY (lunch_id, item_number)
);

-- SUPPLIERS TABLE
CREATE TABLE suppliers (
    supplier_id     VARCHAR(3) PRIMARY KEY,
    supplier_name   VARCHAR(30)
);

-- CONSTANTS TABLE
CREATE TABLE constants (
    business_name         VARCHAR(30),
    business_start_date   DATE,
    lunch_budget          NUMERIC(5,2),
    owner_name            VARCHAR(30)
);

-- Foreign Key Constraints
ALTER TABLE employees
    ADD CONSTRAINT fk_employees_dept_code
    FOREIGN KEY (dept_code)
    REFERENCES departments (dept_code);

ALTER TABLE employees
    ADD CONSTRAINT fk_employees_manager_id
    FOREIGN KEY (manager_id)
    REFERENCES employees (employee_id);

ALTER TABLE LUNCHES
    ADD CONSTRAINT fk_lunches_employees
    FOREIGN KEY (employee_id)
    REFERENCES employees (employee_id);

ALTER TABLE lunch_items
    ADD CONSTRAINT fk_lunch_items_lunches
    FOREIGN KEY (lunch_id)
    REFERENCES lunches (lunch_id);

ALTER TABLE lunch_items
    ADD CONSTRAINT fk_lunch_items_foods
    FOREIGN KEY (Supplier_id, product_code)
    REFERENCES foods (supplier_id, product_code);

ALTER TABLE foods
    ADD CONSTRAINT fk_foods_suppliers
    FOREIGN KEY (supplier_id)
    REFERENCES suppliers (supplier_id)
    ON DELETE CASCADE;
