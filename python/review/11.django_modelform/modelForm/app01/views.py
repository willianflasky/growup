from django.shortcuts import render
from .models import *
from django.forms import Form, ModelForm
from django.forms import widgets as W
from django.forms import fields as F
from django.core.exceptions import ValidationError


class UserInfoModelForm(ModelForm):
    # 假设:一个月免登陆,增加额外字段，不需要进数据库
    is_rmb = F.CharField(widget=F.CheckboxInput())

    class Meta:
        model = UserInfo
        fields = "__all__"
        # exclude = ['u2g']
        labels = {
            'username': "用户名",
            'email': "邮箱",
            'u2g': "组名"
        }
        help_texts = {
            'username': "请输入你的名字."
        }

        # 模块名和widgets重复了,所以把模块名改成W
        # widgets = {
        #     'username': W.Textarea(attrs={'class': 'c1'})
        # }

        error_messages = {
            # 整体的错误信息
            '__all__': {'required': "出错了", 'invalid': "出错了", },
            'username': {'required': "邮箱不能为空", 'invalid': "邮箱格式错误", }
        }

        # 把邮箱格式的正则改成URL正则
        # field_classes = {
        #    'email': F.URLField
        # }

        # 将ctime字段修改成本地时间;
        # 还要修改settings.py  TIME_ZONE = 'Asia/Shanghai' USE_TZ = True
        # localized_fields = ('ctime')

        # 针对一个字段增加清洗数据， 必须有返回值，后面还有其它clean函数等着接数据继续清理。
        def clean_username(self):
            old = self.cleaned_data['username']
            if len(old) < 6:
                raise ValidationError("length must more then 6")
            return old

        # 最后一个联合校验
        # 这里有错，不是某个字段，是全局校验错误在前端显示{{ form.none_field_errors }}
        # 这里最后了，不需要Return
        def clean(self):
            pass


def index(request):
    if request.method == 'GET':
        obj = UserInfoModelForm()
        return render(request, 'index.html', locals())

    elif request.method == 'POST':
        obj = UserInfoModelForm(request.POST)
        if obj.is_valid():
            obj.save()
            # 下面3行和上面obj.save()相等，只是拆开了。
            # instance = obj.save(False)
            # instance.save()   # 只保存本表的数据
            # obj.save_m2m()    # 保存第三方M2M数据

            print(obj.cleaned_data)
            print(obj.errors.as_json)
            # UserInfo.objects.filter(id=1).update(**obj.cleaned_data)
        return render(request, 'index.html', locals())


def user_list(request):
    li = UserInfo.objects.all().select_related('user_type')  # select_related只能加FK
    return render(request, 'user_list.html', locals())


def user_edit(request, nid):
    # 获取当前ID对应的用户信息,
    # 而且放好默认值
    if request.method == 'GET':
        user_obj = UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(instance=user_obj)
        return render(request, 'user_edit.html', locals())

    elif request.method == 'POST':
        user_obj = UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST, instance=user_obj)  # 这里instance=user_obj不写的话，就是新增一条数据
        if mf.is_valid():
            # 保存session, 一个月登录
            # request.session['is_rmb'] = True
            mf.save()
        else:
            print(mf.errors.as_json())

        return render(request, 'user_edit.html', locals())


