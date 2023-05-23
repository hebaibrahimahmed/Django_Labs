from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from staff.models import *
from student.models import *


# Create your views here.
def viewList(req):
    context = {'students': Student.objects.all(), 'staff': Staff.objects.all()}
    # HttpResponseRedirect('student/list_student.html',context)
    return render(req, 'student/list_student.html', context)


def insertStudent(req):
    if req.method == 'GET':
        context = {
            'staff': Staff.objects.all()
        }
        return render(req, 'student/insert_student.html', context)
    else:
        Student.objects.create(username=req.POST['username'],
                               address=req.POST['address'],
                               email=req.POST['email'],
                               password=req.POST['password'],
                               staff_id=Staff.objects.get(id=req.POST['staff_id']))
        return viewList(req)


def updateStudent(req, id):
    if req.method == 'GET':
        context = {'student': Student.objects.get(id=id), 'staff': Staff.objects.all()}
        return render(req, 'student/update_student.html', context)
    else:
        Student.objects.filter(id=id).update(username=req.POST['username'],
                                          address=req.POST['address'],
                                          email=req.POST['email'],
                                          password=req.POST['password'],
                                          staff_id=Staff.objects.get(id=req.POST['staff_id']))
        return viewList(req)


def deleteStudent(req, id):
    Student.objects.filter(id=id).delete()
    return viewList(req)
