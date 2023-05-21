from multiprocessing import context
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect,HttpResponseNotAllowed
from .models import *
from student.models import Student

# Create your views here.
#================list student================
def list(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student/list.html', context)

#====================insert student===============

def insert(request):
    if request.method == "GET":
        staff_objects = Staff.objects.all()
        return render(request, 'student/add.html', {'staff_objects': staff_objects})
    else:
        Student.objects.create(
            name=request.POST['studentname'],
            email=request.POST['email'],
            Password=request.POST['password'],
            staffObj=Staff.objects.get(id=request.POST['staffid'])
        )
        return redirect('/student/')


#=======================================================

def update(request, id):
    if request.method == 'GET':
        student = get_object_or_404(Student, id=id)
        staff_objects = Staff.objects.all()
        context = {'student': student, 'staff_objects': staff_objects}
        return render(request, 'student/update.html', context)
    elif request.method == 'POST':
        student = get_object_or_404(Student, id=id)
        student.name = request.POST['studentname']
        student.staffObj = Staff.objects.get(id=request.POST['staffid'])
        student.save()
        students = Student.objects.all()
        return render(request, 'student/list.html', {'students': students})
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


    #==================================================

def delete(r, id):
    Student.objects.filter(id=id).delete()
    students = Student.objects.all()
    return render(r, 'student/list.html', {'students': students})