from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from django import forms
import json,re
from django.core.exceptions import ValidationError

def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class LoginForm(forms.Form):
    user=forms.CharField(required=True,error_messages={'required':'用户名不能为空.'})
    pwd=forms.CharField(required=True,
                        min_length=6,
                        max_length=10,
                        error_messages={'required':'密码不能为空.','min_length':"至少6位","max_length":'最多10位'}
                        )
    num=forms.IntegerField(error_messages={'required':'密码不能为空.','invalid':'必须输入数字'})
    phone=forms.CharField(validators=[mobile_validate,],
                          error_messages={'required':'密码不能为空.'}
                          )
    #test=forms.CharField(widget=forms.Input(attrs={'class':'c1'}))

    test_choise=(
        (0,'上海'),
        (1,'北京'),
    )
    test=forms.IntegerField(widget=forms.Select(choices=test_choise))

def login(request):
    if request.POST:
        objPost=LoginForm(request.POST)
        ret=objPost.is_valid()
        if ret:
            print(objPost.clean())
        else:
            from django.forms.utils import ErrorDict

            pass
        return render(request,'login.html',{'obj1':objPost})

    else:
        objGet=LoginForm()
        return render(request,'login.html',{'obj1':objGet})

#@csrf_protect  生效
#@crsf_exempt   不生效

def csrf(request):
    return render(request,'csrf.html')

def cookie(request):
    print(request.COOKIES)      #获取用户COOKIE
    obj=render(request,'cookie.html')
    obj.set_cookie('k1','v1')   #写COOKIE给用户
    return obj

#cookie
def log(request):
    if request.method=='POST':
        u=request.POST.get('user')
        p=request.POST.get('pwd')

        if u=='tom' and p=='123':
            print(u)
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

#session
USER_LIST=['alex','eric','hu']

def session_login(request):
    if request.method=='POST':
        u=request.POST.get('user')
        p=request.POST.get('pwd')
        if p =='123' and u in USER_LIST:
            request.session['user']=u       #django帮我们写了cookie给用户.
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
            return redirect('/session_login/')
        return func(request,*args,**kwargs)
    return inner

@auth
def session_index(request):
    user=request.session.get('user',None)
    return render(request,'session_index.html',{'user':user})

@auth
def session_logout(request):
    #del request.session['user']
    request.session.delete(request.session.session_key)
    return redirect('/session_login/')

"""
model操作
1.基本操作
2.进阶
3.双下滑线
    --可以跨表
    --大小于操作

    class UserInfo(models.Model):
        user=models.CharField(max_length=32)
        pwd=models.CharField(max_length=32)

    queryset=UserInfo.objects.all()

    pirnt(queryset.query) --SQL
        [UserInfo对象,UserInfo对象]

    queryset=UserInfo.objects.all().values('user')
    [{'user':'alex'},{'user':'eric'}]

    queryset=UserInfo.objects.all().value_list('user')
    [('alex'),('eric')]

一对多
    class UserType(models.Model):
        caption=models.CharField(max_length=32)

    class UserInfo(models.Model):
        user=models.CharField(max_length=32)
        pwd=models.CharField(max_length=32)
        user_type=models.ForignKey('UserType')
        #user_type_id

    一.创建UserInfo
        1.UserInfo.objects.create(user='alex',pwd=123,user_type=UserType.objects.get(id=2))     #两次操作.
        2.UserInfo.objects.create(user='alex',pwd=123,user_type_id=2)

    二.查询
        1.UserInfo.objects.filter(user='alex')  #单表
        2.查询所有用户类型等于普通用户的所有用户名和密码.
            uid=UserType.objects.get(caption='普通用户').id
            UserInfo.objects.filter(user_type_id=uid)           #两次操作.
        3.queryset=UserInfo.objects.filter(user_type__caption='普通用户')
            UserInfo.objects.filter(user_type__id__gt=2)
            [UserInfo对象,UserInfo对象]
            row=queryset[0]
            row.user
            row.pwd
            row.user_type.id
            row.user_type.caption
            #双下划线解决跨表查询
            #row.外健字段.外建表的字段
        4.queryset=UserInfo.objects.filter(user_type__caption='普通用户').values('user','user_type__caption')
                [{'user':'alex','user_type_caption':'普通用户'},{'user':'eric','user_type_caption':'普通用户'}]
            row queryset[0]
            row['user']
            row['user_type_caption']

三张表跨表操作
    class Something(models.Mode)
        name=models.CharField(max_length=32)

    class UserType(models.Model):
        caption=models.CharField(max_length=32)
        s=models.ForignKey('Something')

    class UserInfo(models.Model):
        user=models.CharField(max_length=32)
        pwd=models.CharField(max_length=32)
        user_type=models.ForignKey('UserType')

        queryset=UserInfo.objects.filter(user_type__s__name='xx')


"""