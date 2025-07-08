from payroll.models import PayrollRecord
from attendance.models import AttendanceRecord
from employees.models import Employee
from django.db.models import Count

def calculate_salary():
    employees = Employee.objects.all()
    for employee in employees:
        attendance_count = AttendanceRecord.objects.filter(employee=employee).count()
        salary = attendance_count * 50000
        PayrollRecord.objects.create(employee=employee, salary=salary)

