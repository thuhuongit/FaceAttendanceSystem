from django.db import models
from employees.models import Employee

class PayrollRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=7)  # VD: "2025-07"
    total_hours = models.FloatField()
    total_salary = models.FloatField()

    def __str__(self):
        return f"{self.employee.name} - {self.month}"
