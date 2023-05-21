from django.urls import path,include
from .views import list, insert ,update , delete


urlpatterns = [
    path('',list),
    path('insert/',insert),
    path('update/',update),
    path('delete/',delete),
]
