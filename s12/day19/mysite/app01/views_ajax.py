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
    pwd=forms.CharField(required=True,error_messages={'required':'密码不能为空.','min_length':'至少6位.','max_length':'最多10位.'},min_length=6,max_length=10)
    num=forms.IntegerField(error_messages={'required':'数字不能为空.','invalid':"必须输入数字"})
    phone=forms.CharField(validators=[mobile_validate,],)

import json
def login(request):
    if request.method == 'POST':
        result={'status':False,'message':None}
        obj=LoginForm(request.POST)
        ret=obj.is_valid()
        if ret:
            print(obj.clean())
            result['status']=True
        else:
            from django.forms.utils import ErrorDict
            error_str=obj.errors.as_json()          #str字典
            result['message']=json.loads(error_str) #str--->dict存到message
        return HttpResponse(json.dumps(result))     #dict--->str

    return render(request, 'login_ajax.html')

