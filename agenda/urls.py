# djangocalendar/urls.py

from django.urls import path, include

urlpatterns = [
    path('', include('cal.urls')),
]