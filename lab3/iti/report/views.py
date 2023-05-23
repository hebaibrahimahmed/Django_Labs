from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from student.views import viewList


# Create your views here.

def listStudent(req):
    return HttpResponse('<h2>Student List</h2>')


def listStaff(req):
    return HttpResponse('<h2>Staff List</h2>')


def mainReport(req):
    return render(req,'report/report.html')
