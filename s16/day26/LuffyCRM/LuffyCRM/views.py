from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.


@login_required
def index(request):
    return render(request,"index.html")


def account_logout(request):
    logout(request)
    return redirect("/")

def account_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            print('user login scuess',user)
            login(request,user)
            return  redirect(request.GET.get('next') or '/')

    return render(request,'login.html')