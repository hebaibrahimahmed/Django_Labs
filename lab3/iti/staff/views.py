from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from staff.models import *


@login_required
def viewList(req):
    context = {'staff': Staff.objects.all()}
    return render(req, 'staff/list_staff.html', context)


def insertStaff(req):
    if req.method == 'GET':
        return render(req, 'staff/insert_staff.html')
    else:
        Staff.objects.create(username=req.POST['username'],
                               address=req.POST['address'],
                               email=req.POST['email'],
                               password=req.POST['password'])
        return viewList(req)


def updateStaff(req, id):
    if req.method == 'GET':
        context = {'staff': Staff.objects.get(id=id)}
        return render(req, 'staff/update_staff.html', context)
    else:
        Staff.objects.filter(id=id).update(username=req.POST['username'],
                                             address=req.POST['address'],
                                             email=req.POST['email'],
                                             password=req.POST['password']
                                           )
        return viewList(req)


def deleteStaff(req, id):
    Staff.objects.filter(id=id).delete()
    return viewList(req)


def getAllStaff(req):
    return Staff.objects.all()