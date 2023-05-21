from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

# Create your views here.
def listStaff(req):
    if(req.method=='GET'):
        res= HttpResponse('list staff works')
        return res
    else:
        return HttpResponse('access denied')

def liststudent(req):
    if(req.method=='GET'):
        res= HttpResponse('list students works')
        return res
    else:
        return HttpResponse('access denied')

def mainreports (req):
    if(req.method=='GET'):
        return render(req,'reports/report.html')
    else:
        return HttpResponse('access denied')