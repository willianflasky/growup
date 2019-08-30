from django.shortcuts import render, redirect
from app01.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
from utils.pager import PageInfo


from django import forms
from django.forms import fields
from django.forms import widgets


# 基于django分页
def test(request):
    user_list = UserInfo.objects.all()
    current_page = request.GET.get('p')

    paginator = Paginator(user_list, 10)
    # paginator下面的方法
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    # page:     page对象

    try:
        page_obj = paginator.page(current_page)
        # page_obj下面的方法
        # has_next              是否有下一页
        # next_page_number      下一页页码
        # has_previous          是否有上一页
        # previous_page_number  上一页页码
        # object_list           分页之后的数据列表
        # number                当前页
        # paginator             paginator对象

    except EmptyPage as e:
        page_obj = paginator.page(1)
    except PageNotAnInteger as e:
        page_obj = paginator.page(1)

    return render(request, 'test.html', locals())


# 自定义分页-推荐
def test2(request):
    all_count = UserInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('p'), 10, all_count, request.path_info, page_range=7)
    user_list = UserInfo.objects.all().order_by('-id')[page_info.start():page_info.end()]

    return render(request, 'test2.html', locals())


class UserForm(forms.Form):
    username = fields.CharField(
        required=True,
        error_messages={'required': '用户名不能为空'},
        widget=widgets.TextInput(attrs={'class': 'form-control'})   # 生成什么HTML插件

    )  # 正则表达式,生成HTML标签
    password = fields.CharField(
        required=True,
        error_messages={'required': '密码不能为空'},
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    )  # 正则表达式,生成HTML标签
    email = fields.EmailField(
        required=True,
        error_messages={'required': '邮箱不能为空', 'invalid': '邮箱格式错误'},
        widget=widgets.EmailInput(attrs={'class': 'form-control'})
    )  # 正则表达式,生成HTML标签

    ut_id = fields.IntegerField(
        required=True,
        widget=widgets.Select(
            attrs={'class': 'form-control'},
            # choices=[(1,'普通用户'),(2,"超级用户")])                                      # 第一步
            # choices=UserType.objects.values_list('id', 'name')                          # 第二步
        )
    )

    # 解决增加用户类型时,需要重启服务
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['ut_id'].widget.choices = UserType.objects.values_list('id', 'name')  # 第三步


def adduser(request):
    if request.method == 'GET':
        obj = UserForm()
        return render(request, "adduser.html", locals())
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/test2/')
        return render(request, 'adduser.html', locals())


def edituser(request, uid):
    if request.method == "GET":
        user = UserInfo.objects.filter(id=uid).first()
        obj = UserForm(initial={'username': user.username, 'password': user.password, "email": user.email, "ut_id": user.ut_id})
        return render(request, 'edituser.html', locals())
    else:
        obj = UserForm(data=request.POST)
        if obj.is_valid():
            UserInfo.objects.filter(id=uid).update(**obj.cleaned_data)
            return redirect('/test2/')
        return render(request, 'edituser.html', {"uid": uid, 'obj': obj})

