from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


#   request:请求信息对象   HttpResponse：响应信息对象

def index(request):

    #return HttpResponse("<h1>welcome python</h1>")
    return render(request,"index.html")

def special_case_2003(request):

    return HttpResponse("2003")

def year_archive(request,year):

    return HttpResponse(year)


def month_archive(request,month,year,): # 一定和关键字参数对应好

    return HttpResponse("year: %s  month: %s"%(year,month))

def article_detail(req,year,month,id):


    return HttpResponse(id)
def timer(req):

    # 如何把后端的变量嵌套进入前端页面

    t=datetime.datetime.now()
    a=1
    b=[1,23,4]

    #return render(req,"timer.html",{"Time":t,"a":a,"b":b})  # timer.html是一个模板文件
    return render(req,"timer.html",locals())  # timer.html是一个模板文件
    #return HttpResponse("<h1>Current time:%s</h1>"%t)


def login(request):

    # print("method",request.method)
    if request.method=="POST":

        username=request.POST.get("username",None)
        passsword=request.POST.get("pwd",None)

        if username=="alex" and passsword=="123":

            # return HttpResponse("登录成功！")
            return redirect("/back/")

    return render(request,"login.html")

import datetime


def back(req):
    obg_list=Books.objects.all()  # [obj,obj...]



    return render(req,"back.html",locals())


def template(request):

    name="hello"
    l=[111,222,333]
    d={"name":"alex","age":35}
    class Person():
        id=3
        age=22
        name="egon"

    class Person1():
        id=3
        age=12
        name="egon"

    name_list=[Person(),Person(),Person1()]


    return render(request,"template.html",locals())

from blog.models import *

def add_books(request):
    # 创建记录两种方式： 1 create  2 save
    #Books.objects.create(title="python",author="egon",price=12,pub_date="2000 12 12")
    #注意：pub_date因为是Datetime数据类型，所以，格式固定：-------"2000-12-12"

    b=Books(title="JAVA",author="yuan",price=12.12)
    b.save()

    #return HttpResponse("添加成功！")
    return redirect("/back/")

def delete_books(req):

    nid=req.GET.get("id")
    Books.objects.filter(id=nid).delete()
    #Books.objects.filter(title="JAVA").delete()

    return redirect("/back/")

def edit_books(req):
    nid = req.GET.get("id")

    # b=Books.objects.get(id=nid) #filter取到的是集合对象，get是单一对象
    # b.price=100
    # b.save()   # 效率较低


    Books.objects.filter(id=nid).update(price=100)
    return redirect("/back/")







