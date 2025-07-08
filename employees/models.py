from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/')  # Ảnh khuôn mặt
    position = models.CharField(max_length=100)
    hourly_rate = models.FloatField(default=20000.0)

    def __str__(self):
        return f"{self.name} ({self.employee_code})"
