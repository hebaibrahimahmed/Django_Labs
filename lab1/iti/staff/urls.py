from django.urls import path,include
from .views import liststaff, insertstaff ,updatestaff , deletestaff


urlpatterns = [
    path('',liststaff),
    path('insert/',insertstaff),
    path('update/',updatestaff),
    path('delete/',deletestaff),
]
