from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Department, Employee


class DepartmentModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="HR")

    def test_department_creation(self):
        self.assertEqual(self.department.name, "HR")
        self.assertTrue(isinstance(self.department, Department))

    def test_department_str(self):
        self.assertEqual(str(self.department), "HR")


class EmployeeModelTest(TestCase):
    def setUp(self):
        # Create a department
        self.department = Department.objects.create(name="IT")
        # Create an employee
        self.employee = Employee.objects.create(
            employee_id="E12345",
            email="john.doe@example.com",
            first_name="John",
            last_name="Doe",
            department=self.department,
            salary=60000.00,
            password="testpassword123",
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.email, "john.doe@example.com")
        self.assertEqual(self.employee.first_name, "John")
        self.assertEqual(self.employee.last_name, "Doe")
        self.assertEqual(self.employee.department, self.department)
        self.assertEqual(self.employee.salary, 60000.00)

    def test_employee_str(self):
        expected_str = "John Doe (john.doe@example.com)"
        self.assertEqual(str(self.employee), expected_str)

    def test_unique_email_constraint(self):
        with self.assertRaises(Exception):
            Employee.objects.create(
                employee_id="E54321",
                email="john.doe@example.com",  # Duplicate email
                first_name="Jane",
                last_name="Doe",
                department=self.department,
                salary=70000.00,
                password="anotherpassword",
            )

    def test_primary_key_unique(self):
        # Attempt to create another employee with same employee_id
        with self.assertRaises(Exception):
            Employee.objects.create(
                employee_id="E12345",  # Same primary key
                email="jane.doe@example.com",
                first_name="Jane",
                last_name="Doe",
                department=self.department,
                salary=70000.00,
                password="anotherpassword",
            )
