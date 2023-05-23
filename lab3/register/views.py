from django.shortcuts import render

import student.views
from staff.models import *
from student.models import *
from student.views import *
from .forms import *
# Create your views here.
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def registerForm(req):
    if req.method == 'GET':
        context = {'staff': Staff.objects.all()}
        context['form']=CreateRegisterForm()
        return render(req, 'register/register.html', context)
    else:
        if Staff.objects.filter(email=req.POST['email']).exists():
            context = { 'message': 'Email already exists' }
            context['form'] = CreateRegisterForm()
            return render(req, 'register/register.html', context)
        else:
            Student.objects.create(
                username=req.POST['username'],
                address=req.POST['address'],
                email=req.POST['email'],
                password=req.POST['password'],
                staff_id=Staff.objects.get(id=req.POST['staff_id']))
            return student.views.insertStudent(req)