from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


# Create your views here.
def liststaff(req):
    if (req.method == 'GET'):
        res = HttpResponse('list staff works')
        return res
    else:
        return HttpResponse('access denied')

def insertstaff(req):
    return JsonResponse({'id': 1, 'name': 'heba'})

def updatestaff(req):
        return JsonResponse({'id': 1, 'name': 'heba'})

def deletestaff(r):
    if (r.method == 'GET'):
        return HttpResponseRedirect('/staff')
    else:
        return HttpResponse('access denied')


