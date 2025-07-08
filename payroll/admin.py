from django.contrib import admin
from .models import PayrollRecord

@admin.register(PayrollRecord)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'month', 'total_hours', 'total_salary')
