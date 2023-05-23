from django.urls import path, include
from index.views import *


urlpatterns = [
    path('', home, name='')
]