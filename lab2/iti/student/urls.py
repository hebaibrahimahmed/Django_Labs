from django.urls import path,include
from .views import list, insert ,update , delete


urlpatterns = [
    path('',list),
    path('insert/',insert, name='insert'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/',delete, name='delete'),
]
