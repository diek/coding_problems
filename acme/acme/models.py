from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)

    # Custom primary key: a unique character
    employee_id = models.CharField(max_length=10, primary_key=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "employee_id", "department"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
