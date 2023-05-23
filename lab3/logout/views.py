from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
from login.forms import CreateLoginForm


def logoutSession(request):
    context={}
    form = CreateLoginForm()
    context['form'] = form
    request.session.clear()
    return render(request, 'login/login.html', context)