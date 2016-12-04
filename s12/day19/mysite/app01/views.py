from django.shortcuts import render,HttpResponse

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

