from django.shortcuts import render
from .models import PayrollRecord

def payroll_view(request):
    payrolls = PayrollRecord.objects.select_related('employee').order_by('-month')
    return render(request, 'payroll/payroll.html', {'payrolls': payrolls})
