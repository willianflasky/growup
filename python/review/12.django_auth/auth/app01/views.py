from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next') or '/')
        else:
            error = "用户名或者密码错误!"
    return render(request, 'login.html', locals())


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


@login_required(login_url="/login/")
def index(request):
    return render(request, 'index.html', locals())
