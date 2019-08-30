from django.shortcuts import render, HttpResponse, redirect
import time
from app01.models import *
from django.views.decorators.cache import cache_page
from utils import BaseReponse
import json
from django.forms import Form
from django.forms import fields
# Create your views here.


class LoginForm(Form):
    username = fields.CharField(error_messages={'required': "用户名不能为空"})
    password = fields.CharField(error_messages={'required': "密码不能为空"})


def index(request):
    return render(request, 'index.html', locals())


def show(request):
    if request.method == 'GET':
        return render(request, 'show.html', locals())
    else:
        user_list = UserInfo.objects.all()
        ret = BaseReponse()
        try:
            user_list = UserInfo.objects.values('id', 'username')
            user_list = list(user_list)
            ret.status = True
            ret.data = user_list
        except Exception as e:
            ret.error = "获取数据失败"
        data = json.dumps(ret.__dict__)
        return HttpResponse(data)


def login(request):
    response = BaseReponse()
    try:
        obj = LoginForm(request.POST)
        if obj.is_valid():
            v = UserInfo.objects.filter(**obj.cleaned_data).first()
            if v:
                request.session['username'] = v.username
                response.status = True
            else:
                response.status = False
                response.error = "用户名或密码错误"
        else:
            print(obj.errors)
            response.status = False
            response.error = obj.errors
    except Exception as e:
        response.status = False
    # 将responese对象的静态字段 转成 字典(response.__dict__)
    # ensure_ascii=False解决中文访问
    return HttpResponse(json.dumps(response.__dict__, ensure_ascii=False))


def home(request):
    return render(request, 'home.html', locals())


def logout(request):
    request.session.clear()
    return HttpResponse('done')


def formupload(request):
    if request.method == 'GET':
        return render(request, 'formupload.html')
    else:
        obj = request.FILES.get('fffff')
        f = open(obj.name, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        return render(request, 'formupload.html', locals())


def ajaxupload(request):
    import os
    response = BaseReponse()
    if request.method == 'GET':
        return render(request, 'ajaxupload.html')
    else:
        try:
            obj = request.FILES.get('fffff')
            file_path = os.path.join('static', obj.name)
            f = open(file_path, 'wb')
            for chunk in obj.chunks():
                f.write(chunk)
            f.close()
            response.status = True
            response.data = file_path
        except Exception as e:
            response.status = False
        return HttpResponse(json.dumps(response.__dict__, ensure_ascii=False))


def ifreamupload(request):
    import os
    response = BaseReponse()
    if request.method == 'GET':
        return render(request, 'ifreamupload.html')
    else:
        try:
            obj = request.FILES.get('fffff')
            file_path = os.path.join('static', obj.name)
            f = open(file_path, 'wb')
            for chunk in obj.chunks():
                f.write(chunk)
            f.close()
            response.status = True
            response.data = file_path
        except Exception as e:
            response.status = False
        return HttpResponse(json.dumps(response.__dict__, ensure_ascii=False))
