from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from cmdb import models

def home(request):
    if request.method=='POST':
        u = request.POST.get('user',None)
        e = request.POST.get('email',None)
        m=models.UserInfo.objects.filter(user=u).count()
        if m >= 1:
            return redirect('/index/')
    return render(request,'home.html')


def index(request):
    #return HttpResponse("123")
    #return redirect('http://baidu.com')
    #return redirect('/index/')
    if request.method=='POST':
        u = request.POST.get('user',None)
        e = request.POST.get('email',None)
        models.UserInfo.objects.create(user=u,email=e)


    data_list=models.UserInfo.objects.all()

    return render(request,'index.html',{'data':data_list})

