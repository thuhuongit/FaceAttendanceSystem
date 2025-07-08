from django.shortcuts import render
from .models import AttendanceRecord

def checkin_view(request):
    return render(request, 'attendance/checkin.html')

def report_view(request):
    records = AttendanceRecord.objects.all().order_by('-date')
    return render(request, 'attendance/report.html', {'records': records})
