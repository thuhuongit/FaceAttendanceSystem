from django.urls import path
from . import views

urlpatterns = [
    path('checkin/', views.checkin_view, name='checkin'),
    path('report/', views.report_view, name='report'),
]
