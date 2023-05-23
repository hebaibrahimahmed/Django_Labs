from django.urls import path, include
from staff.views import *

urlpatterns = [
    path('list/', viewList, name='liststaff'),
    path('delete/<int:id>', deleteStaff, name='deletestaff'),
    path('insert/', insertStaff, name='insertstaff'),
    path('update/<int:id>', updateStaff, name='updatestaff'),
]