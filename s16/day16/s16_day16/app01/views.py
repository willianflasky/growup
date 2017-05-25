from django.shortcuts import render,HttpResponse
from django.template import Template, Context

from app01.models import *
# Create your views here.
import datetime

def timer(request):

    times=datetime.datetime.now()

    # templates=Template("<h1>the current time:{{t}}</h1>")
    #
    # contexts=Context({"t":t})
    #
    # ret=templates.render(contexts)
    #
    # return HttpResponse(ret)
    # t=datetime.date(1993, 5, 2)

    x=10

    y=[11,22]

    a="<a href='#'>跳转</a>"

    s="hello asdgsdf gsFGSDA GSFDGDSF"
    s2="hello world python python python python python python python"

    value8 = 'http://www.baidu.com/?a=1&b=3'

    L=[[1,2,3],[4,5,6],[7,8,9]]
    obj_list=[]

    z=10
    return render(request,"timer.html",locals())


def validate(req):

    return HttpResponse("success")
def index(req):

    #return render(req,"index.html")
    return render(req,"index_new.html")

def classes(req):

    #return render(req,"classes.html")
    return render(req,"classes_new.html")


def addbook(req):

    # 多对一的插入方式一
    #Book.objects.create(title="python葵花宝典",publication_date="2017-5-13",price=10,publisher_id=2)

    # filter的queryset的集合对象   [obj1,]
    #obj=Publisher.objects.filter(name="北京大学出版社")[0]

    # 多对一的插入方式二  publisher = obj
    #Book.objects.create(title="python葵花宝典2",publication_date="2017-5-14",price=10,publisher=obj)


    # 多对多 添加

    #实现：   对一本书对象绑定一个或者多个作者对象

    #author_obj=Author.objects.filter(name="yuan")[0]
    #book_obj=Book.objects.filter(id=1)[0]

    #book_obj.author:id=3的book对象所有关联的作者集合
    #print("*****",book_obj.author.all())  # ***** <QuerySet [<Author: alex>, <Author: egon>]>
    #book_obj.author.add(author_obj)


    #实现：   对一个作者对象对象绑定一个或者多个书对象
    author_obj = Author.objects.filter(name="yuan")[0]
    book_list = Book.objects.filter(id__lte=2)
    print("------",author_obj.book_set.all())
    author_obj.book_set.add(*book_list)#


    return HttpResponse("添加成功")



def query(req):
    print("okokkok")

    #ret=Book.objects.filter(id__gt=1).values("price","title")
    #print("ret",ret)  # ret <QuerySet [{'price': Decimal('10.00')}, {'price': Decimal('10.00')}, {'price': Decimal('100.00')}]>
    #ret <QuerySet [{'price': Decimal('10.00'), 'title': 'python葵花宝典2'}, {'price': Decimal('10.00'), 'title': 'linux'}, {'price': Decimal('100.00'), 'title': '大数据'}]>

    # ret = Book.objects.filter(id__gt=1).values_list("price", "title")
    # print(ret) # [(Decimal('10.00'), 'python葵花宝典2'), (Decimal('10.00'), 'linux'), (Decimal('100.00'), '大数据')]>


    #ret=Book.objects.filter(id__gt=1)

    # for obj in ret:  #[obj,obj]
    #     print(obj)
    #
    # Book.objects.filter(id__gt=1).update(title="yuan")

    # for obj in ret:  #[obj,obj]
    #     print(obj)

    # 优化缓存方法   exists    iterator
    # if ret.exists():
    #     print("ok")

    # iter=ret.iterator()
    #
    # for i in iter:
    #     print(i)
    #
    # for i in iter:
    #     print(i)


   #-----------------------------------------------
    # ---------------------------------------------------重点
    # -----------------------------------------------

    # ret=Book.objects.get(id=3)
    # print(ret.title)
    # print(ret.price)
    # print(ret.publisher_id)
    # print(ret.publisher)
#-------------------------------------------------------------------------
    # ret=Book.objects.filter(author__name="alex").values("title","price")
    # print(ret)


    # ret=Publisher.objects.filter(book__title="python葵花宝典").values("city")
    # print(ret)

    # ret=Book.objects.filter(title="python葵花宝典").values("publisher__city")
    # print(ret)





    return HttpResponse(".....")