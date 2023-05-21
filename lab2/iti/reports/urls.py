from django.urls import path,include
from .views import listStaff,liststudent, mainreports


urlpatterns = [
    path('liststaff/',listStaff),
    path('liststudent/',liststudent),
    path('mainreports/',mainreports),
]
