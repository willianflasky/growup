from django.shortcuts import render
from django.shortcuts import HttpResponse,Http404
from django.shortcuts import redirect
# Create your views here.
from cmdb import models
import datetime

def home(request):
    if request.method=='POST':
        u = request.POST.get('user',None)
        e = request.POST.get('email',None)
        m=models.UserInfo.objects.filter(user=u).count()
        if m >= 1:
            return redirect('/index/')
        else:
            return HttpResponse(status=403)

    return render(request,'home.html')


def delete(request):
    if request.method=="POST":
        u = request.POST.get('user',None)
        m=models.UserInfo.objects.filter(user=u).delete()
    return render(request, 'delete.html')


# def index(request):
#     #return HttpResponse("123")
#     #return redirect('http://baidu.com')
#     #return redirect('/index/')
#     if request.method=='POST':
#         u = request.POST.get('user',None)
#         e = request.POST.get('email',None)
#         ret=models.UserInfo.objects.filter(user=u).count()
#         if ret >= 1:
#             return redirect('/index/')
#         else:
#             if len(u) == 0 or len(e) == 0:
#                 return redirect('/index/')
#             else:
#                 models.UserInfo.objects.create(user=u,email=e)
#
#     data_list=models.UserInfo.objects.all()
#
#     return render(request,'index.html',{'data':data_list})


def hours_ahead(request,offset):
    try:
        offset=int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def first(request):
    return render(request,'first.html')


def detail(request,p1,p2):
    print(p1,p2)
    return HttpResponse("OK")
######################################

USER_LIST=[]
for item in range(94):
    temp={'id':item,'username':'alex'+str(item),'email':'email'+str(item)}
    USER_LIST.append(temp)

def index(request,page):
    page=int(page)
    start = (page-1)*10
    end = page * 10
    user_list = USER_LIST[start:end]
    return render(request,'i.html',{'user_list':user_list})

def detail(request,nid):
    nid=int(nid)
    current_detail_dict = USER_LIST[nid]
    return render(request,'detail.html',{'current_detail_dict':current_detail_dict})


def template(request):
    return render(request,
                  'template.html',
                  {'k1':'V1','k2':[11,22,33],'k3':{'nid':12,'name':'alex'}}
                )


def assets(request):
    assets_list=[]
    for i in range(10):
        temp={'hostname':'h1'+str(i),'port':80}
        assets_list.append(temp)

    return render(request, 'assets.html',{'assets_list':assets_list})


def userinfo(request):
    user_list=[]
    for i in range(10):
        temp={'username':'h1'+str(i),'salary':80}
        user_list.append(temp)
    return render(request,'userinfo.html',{'user_list':user_list})


import json

def ajax_demo(request):
    ret={'status':False,'message':""}
    if request.method == 'POST':
        user=request.POST.get('user',None)
        pwd=request.POST.get('pwd',None)
        if user=='111' and pwd=='222':
            ret['status'] =True
            return HttpResponse(json.dumps(ret))

        else:
            ret['message']="用户名或者密码错误"
            return HttpResponse(json.dumps(ret))

    return render(request,'ajax_demo.html')
