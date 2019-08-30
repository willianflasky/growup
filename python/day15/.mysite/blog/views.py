from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    return HttpResponse("welcome!")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'alex' and password == '123':
            return HttpResponse("OK")
        else:
            return HttpResponse("password error!")

    return render(request, 'login.html')

from blog.models import *


def add_books(request):
    # 创建记录两种方式: 1.Create, 2.save
    # Books.objects.create(title='python', author='agon', price='12', pub_date='2017-12-12')
    # return HttpResponse("添加成功!")
    b = Books(title='java', author='hanhan', price='12.12', pub_date='2017-12-12')
    b.save()
    return redirect("/back/")
