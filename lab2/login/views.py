from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def loginFrom(req):
    return render(req, 'login/login.html')