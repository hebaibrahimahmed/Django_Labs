from django.urls import path, include

from report.views import *

urlpatterns = [
    path('liststudent/', listStudent),
    path('liststaff/', listStaff),
    path('mainreport/', mainReport),
]
