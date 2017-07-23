from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from crm.models import *
# Create your views here.


@login_required(login_url='/login/')
def index(request):

    return render(request, 'index.html', locals())


def web_logout(request):
    logout(request)
    return redirect('/')


def web_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next') or '/')
    return render(request, 'login.htm')


def customer_list(request):
    return HttpResponse('ok')


def need_followup(request):
    return HttpResponse('ok')