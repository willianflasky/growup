from django.shortcuts import render
from app01.models import *
# Create your views here.

from django.forms import Form, fields, widgets


class UserInfoForm(Form):
    username = fields.CharField(max_length=32)
    email = fields.EmailField()
    user_type = fields.ChoiceField(choices=UserType.objects.values_list('id', 'caption'))

    # 为了增加caption数据不需要重启APP。
    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields['user_type'].choices = UserType.objects.values_list('id', 'caption')


def index(request):
    if request.method == 'GET':
        obj = UserInfoForm()
        return render(request, 'index.html', locals())

    elif request.method == 'POST':
        obj = UserInfoForm(request.POST)
        if obj.is_valid():
            UserInfo.objects.create(
                username=obj.cleaned_data['username'],
                email=obj.cleaned_data['email'],
                user_type_id=obj.cleaned_data['user_type']
            )
            # UserInfo.objects.filter(id=1).update(**obj.cleaned_data)
        return render(request, 'index.html', locals())
