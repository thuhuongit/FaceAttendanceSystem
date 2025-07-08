from django.db import models
from employees.models import Employee
from django.utils import timezone

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    date = models.DateField(auto_now_add=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"
