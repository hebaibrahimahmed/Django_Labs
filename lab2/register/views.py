
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseNotAllowed
from .models import Staff
from student.views import insert

def registerForm(request):
    if request.method == 'GET':
        context = {'staff': Staff.objects.all()}
        return render(request, 'register/register.html', context)
    else:
        return insert(request)
