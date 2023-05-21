from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

# Create your views here.
def list(req):
    if(req.method=='GET'):
        res= HttpResponse('list students works')
        return res
    else:
        return HttpResponse('access denied')

def insert (req):
    if(req.method=='GET'):
        return render(req,'student/insert.html')
    else:
        return HttpResponse('access denied')

def update (req):
    if(req.method=='GET'):
        return render(req,'student/update.html')
    else:
        return HttpResponse('access denied')

def delete (r):
    if(r.method=='GET'):
        return HttpResponseRedirect('/student')
    else:
        return HttpResponse('access denied')