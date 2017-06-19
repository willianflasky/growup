from django.shortcuts import render,HttpResponse

# Create your views here.

from django import forms
from app01 import models

class IndexForm(forms.Form):
    c=models.UserType.objects.all().values_list('id','caption')
    print(c)
    user_type_id=forms.IntegerField(widget=forms.Select(choices=c))

    def __init__(self,*args,**kwargs):
        #父类的构造方法,1.获取所有表态字段,2.fields=[]
        super(IndexForm,self).__init__(*args,**kwargs)
        self.fields['user_type_id'].widget.choices=models.UserType.objects.all().values_list('id','caption')

def index(request):

    # c=models.UserType.objects.all().count()
    # print(c)

    form = IndexForm()
    from django.db.models import Q
    con=Q()
    q1=Q()
    q1.connector='OR'
    q1.children.append(('id',1))
    q1.children.append(('id',2))
    q1.children.append(('id',3))
    q2=Q()
    q2.connector='OR'
    q2.children.append(('caption','CE1'))
    q2.children.append(('caption','CE2'))

    con.add(q1,'AND')
    con.add(q2,'AND')

    obj=models.UserType.objects.filter(con)
    for item in obj:
        print(item.id,item.caption)

    return render(request,'index.html',{'form':form})


def add_user_type(request):
    q=request.GET.get('q',None)
    if q:
        models.UserType.objects.create(caption=q)
    return HttpResponse(q)


#F:
#models.UserInfo.objects.fileter().update(salary=F('salary')+500)
#Q:
#构造搜索条件


def add_boy(request):
    boy=request.GET.get('v',None)
    if boy:
        models.Boy.objects.create(username=boy)
    return HttpResponse(boy)


def add_girl(request):

    girl=request.GET.get('v',None)
    if girl:
        models.Girl.objects.create(name=girl)
    return HttpResponse(girl)

def boy_to_girl(request):
    """
    #增加数据
    g1=models.Girl.objects.get(id=1)
    b1=models.Boy.objects.get(id=2)
    g1.b.add(b1)

    ####
    bs=models.Boy.objects.all()
    g1.b.add(*bs)
    """

    #查询数据
    #g1=models.Girl.objects.get(id=1)
    #g1.b.add(*[1,2,3,4])
    # r=models.Girl.objects.all().values('id','name','b__username')
    # print(r)
    # print(r.query)

    r=models.Boy.objects.all().values('id','username','girl__name')
    print(r)
    print(r.query)

    return HttpResponse('OK')



def md(request):
    print('views.md')
    return HttpResponse('ok')


from django.views.decorators.cache import cache_page

@cache_page(5)
def cache(request):
    import time
    c=time.time()
    return render(request,'cache.html',{'c':c})


def page(request):
    # for i in range(25,100):
    #     models.UserType.objects.create(caption='CO'+str(i))
    current_page=request.GET.get('p',1)
    current_page=int(current_page)
    start=(current_page-1)*10
    end=current_page*10
    type_list=models.UserType.objects.all()[start:end]

    total=models.UserType.objects.all().count()
    a,b=divmod(total,10)
    if b==0:
        pass
    else:
        a=a+1

    list_page=[]
    if current_page <=1:
        prev="<a href=javascript:void(0)'>上一页</a>"
    else:
        prev="<a href='/page?p=%s'>上一页</a>" %(current_page-1)

    list_page.append(prev)
    for i in range(1,a+1):
        if i==current_page:
            temp="<a class='active' href='/page?p=%s'>%s</a>"%(i,i)
        else:
            temp="<a href='/page?p=%s'>%s</a>"%(i,i)
        list_page.append(temp)


    if current_page >=1 and current_page >= a:
        post="<a href=javascript:void(0)'>下一页</a>"
    else:
        post="<a href='/page?p=%s'>下一页</a>" %(current_page+1)
    list_page.append(post)

    str_page=''.join(list_page)
    from django.utils.safestring import mark_safe
    str_page=mark_safe(str_page)

    return render(request,'page.html',{'type_list':type_list,'str_page':str_page})


from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def page1(request):
    # customer_list=models.UserType.objects.all()
    # paginator=Paginator(customer_list,10)
    # page = request.GET.get('p')
    # try:
    #     customer_objs=paginator.page(page)
    # except PageNotAnInteger:
    #     customer_objs=paginator.page(1)
    # except EmptyPage:
    #     customer_objs=paginator.page(paginator.num_pages)
    return render(request,'page1.html',{'customer_list':customer_objs})



def page2(request):
    customer_list=models.UserType.objects.all()
    paginator=Paginator(customer_list,10)
    page = request.GET.get('p')
    try:
        customer_objs=paginator.page(page)
    except PageNotAnInteger:
        customer_objs=paginator.page(1)
    except EmptyPage:
        customer_objs=paginator.page(paginator.num_pages)

    return render(request,'page2.html',{'customer_list':customer_objs})


from app01.page import Pager

def user_list(request):
    # for item in range(100,500):
    #     temp={'username':'name%d'%item,'age':item}
    #     models.UserList.objects.create(**temp)
    current_page=request.GET.get('page',1)
    page_obj=Pager(current_page)
    all_item=models.UserList.objects.count()
    page_str=page_obj.page_str(all_item,"/user_list/?page=")
    result=models.UserList.objects.all()[page_obj.start:page_obj.end]
    return render(request,'user_list.html',{'result':result,'page_str':page_str})


