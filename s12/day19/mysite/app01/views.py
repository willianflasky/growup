from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django import forms
import re
from django.core.exceptions import ValidationError
##自定义
def mobile_validate(value):
    mobile_re=re.compile(r'^(13[0-9])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号格式错误.')

class LoginForm(forms.Form):
    user=forms.CharField(required=True,error_messages={'required':'用户名不能为空.'})
    pwd=forms.CharField(required=True,min_length=6,max_length=10,
                        error_messages={'required':'密码不能为空.','min_length':'至少6位.','max_length':'最多10位.'})
    num=forms.IntegerField(error_messages={'required':'数字不能为空.','invalid':"必须输入数字"})
    phone=forms.CharField(validators=[mobile_validate,],)
    #test=forms.CharField(widget=forms.TextInput(attrs={'k1':123}))
    test_choices=(
        (0,'上海'),
        (1,'北京'),
    )
    test = forms.IntegerField(widget=forms.Select(choices=test_choices))

import json
def login(request):
    if request.POST:
        objPost=LoginForm(request.POST)
        ret=objPost.is_valid()
        if ret:
            print(objPost.clean())
        else:
            from django.forms.utils import  ErrorDict
            for k,v in objPost.errors.items():
                print("ERROR:",k,v)

        return render(request,'login.html',{'obj1':objPost})
    else:
        objGet=LoginForm()
    return render(request, 'login.html',{'obj1':objGet})



def csrf(request):
    return render(request,'csrf.html')

def cookie(request):
    print(request.COOKIES)
    obj= HttpResponse(request,'cookie.html')
    obj.set_cookie('k1','v1')
    return obj


def log(request):
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u=='alex' and p =='123':
            red=redirect('/index/')
            red.set_cookie('username',u)
            return red
        else:
            return render(request,'log.html')

    else:
        return render(request,'log.html')

def index(request):
    user=request.COOKIES.get('username')
    if user:
        return render(request,'index.html',{'user':user})
    else:
        return redirect('/log/')


def session_login(request):
    if request.method == 'POST':
        u=request.POST.get('user',None)
        p=request.POST.get('pwd',None)
        if u =='alex' and p =='123':
            request.session['user']=u
            return  redirect('/session_index/')

    return render(request,'session_login.html')

"""
def session_index(request):
    user=request.session.get('user',None)
    if not user:
        return redirect('/session_login/')
    else:
        return render(request,'session_index.html',{'user':user})
"""

def auth(func):
    def inner(request,*args,**kwargs):
        user=request.session.get('user',None)
        if not user:
            return redirect('/session_login')
        return func(request,*args,**kwargs)
    return inner


@auth
def session_index(request):
    user=request.session.get('user',None)
    return render(request,'session_index.html',{'user':user})

@auth
def session_logout(request):
    del request.session['user']
    return redirect('/session_login/')




class AddForm(forms.Form):
    a=forms.IntegerField()
    b=forms.IntegerField()

def calc_index(request):
    if request.method == 'POST':
        form = AddForm(request.POST)

        if form.is_valid():
            a=form.cleaned_data['a']
            b=form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:

        form=AddForm()
    return render(request,'calc_index.html',{'form':form})


def form(request):
    error=False
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            error=True
        else:
            books=UserInfo.objects.filter(user_icontains=q)
            return render(request,'form.html',{'books':books})

    return render(request,'form.html',{'error':error})
