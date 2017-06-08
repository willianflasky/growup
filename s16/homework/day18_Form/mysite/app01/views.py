from django.shortcuts import render, HttpResponse, redirect
from app01.models import *
# Create your views here.
from utils.pager import PageInfo
from django import forms
from django.forms import fields
from django.forms import widgets
import json


class LoginForm(forms.Form):
    username = fields.CharField(
        required=True,
        error_messages={'required': "用户名不能为空"},
        widget=widgets.TextInput(attrs={'id': "name", 'name': 'username', 'placeholder': "Username"})
    )
    password = fields.CharField(
        required=True,
        error_messages={'required': "密码不能为空"},
        widget=widgets.PasswordInput(attrs={'id': 'password', 'placeholder': 'Password', 'name': 'password'})
    )


def login(request):
    username = request.session.get('username', '')
    if username:
        return redirect('/index.html')

    if request.method == 'GET':
        obj = LoginForm()
        return render(request, 'login.html', locals())
    else:
        obj = LoginForm(request.POST)
        status = {'status': True, 'error': None}

        if obj.is_valid():
            if Users.objects.filter(username=obj.cleaned_data['username'], password=obj.cleaned_data['password']).first():
                request.session['username'] = obj.cleaned_data['username']
                request.session['password'] = obj.cleaned_data['password']
                return HttpResponse(json.dumps(status))
            else:
                status['status'] = False
                status['error'] = "用户名或者密码错误"
                return HttpResponse(json.dumps(status))
        else:
            return render(request, 'login.html', locals())


def index(request):
    username = request.session.get('username', '')
    if not username:
        return redirect('/login/')

    all_count = Hosts.objects.all().count()
    page_info = PageInfo(request.GET.get('p'), 10, all_count, request.path_info, page_range=11)
    user_list = Hosts.objects.all().order_by('-id')[page_info.start():page_info.end()]
    return render(request, 'index.html', locals())


def logout(request):
    request.session.clear()
    return redirect("/")


class AddForm(forms.Form):
    ip = fields.CharField(
        required=True,
        error_messages={'required': "IP不能为空"},
        widget=widgets.TextInput(attrs={"class": "form-control", "name": "ip", "placeholder": "1.1.1.1"})
    )
    port = fields.CharField(
        required=True,
        error_messages={"required": "Port不能为空"},
        widget=widgets.TextInput(attrs={"class": "form-control", "name": "port", "placeholder": "22"})
    )
    hostuser = fields.CharField(
        required=True,
        error_messages={"required": "主机用户不能为空"},
        widget=widgets.TextInput(attrs={"class": "form-control", "name": "hostuser", "placeholder": "root"})
    )
    hostpass = fields.CharField(
        required=True,
        error_messages={"required": "主机密码不能为空"},
        widget=widgets.PasswordInput(attrs={"class": "form-control", "name": "hostpass", "placeholder": "111111"})
    )

    bussiness_id = fields.IntegerField(
        required=True,
        widget=widgets.Select(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['bussiness_id'].widget.choices = Bussiness.objects.values_list('id', 'bussline')


def addhost(request):
    username = request.session.get('username', '')
    if not username:
        return redirect("/login/")

    if request.method == 'GET':
        obj = AddForm()
        return render(request, 'addhost.html', locals())
    else:
        obj = AddForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            Hosts.objects.create(**obj.cleaned_data)
            return redirect('/addhost/')
        return render(request, 'addhost.html', locals())
