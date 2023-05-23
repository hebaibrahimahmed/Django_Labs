from django.urls import path, include
from student.views import *

urlpatterns = [
    path('list/', viewList, name='liststudents'),
    path('delete/<int:id>', deleteStudent, name='deletestudent'),
    path('insert/', insertStudent, name='insertstudent'),
    path('update/<int:id>', updateStudent, name='updatestudent'),
]