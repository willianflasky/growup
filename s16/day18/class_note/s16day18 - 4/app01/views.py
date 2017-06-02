from django.shortcuts import render,HttpResponse,redirect
from app01 import models
#
# def create_temp_data(request):
#     for i in range(104,1004):
#         models.UserInfo.objects.create(
#             username='root%s' %i,
#             password="123123",
#             email='root%s@qq.com' %i
#         )
#     return HttpResponse('创建成功')

def users1(request):

    from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
    current_page = request.GET.get('p')
    user_list = models.UserInfo.objects.all()

    paginator = Paginator(user_list,10)
    # per_page: 每页显示条目数量
    # count:    数据总个数
    # num_pages:总页数
    # page_range:总页数的索引范围，如: (1,10),(1,200)
    try:
        page_obj = paginator.page(current_page)
    except EmptyPage as e:
        page_obj = paginator.page(1)
    except PageNotAnInteger as e:
        page_obj = paginator.page(1)
    # has_next              是否有下一页
    # next_page_number      下一页页码
    # has_previous          是否有上一页
    # previous_page_number  上一页页码
    # object_list           分页之后的数据列表
    # number                当前页
    # paginator             paginator对象
    return render(request,'users1.html',{'page_obj':page_obj})


from utils.page import PageInfo

def users2(request):
    all_count = models.UserInfo.objects.all().count()

    page_info = PageInfo(request.GET.get('p'),10,all_count,request.path_info)

    user_list = models.UserInfo.objects.all().order_by('-id')[page_info.start():page_info.end()]


    return render(request,'users2.html',{'user_list':user_list,'page_info': page_info})

from django import forms
from django.forms import fields
from django.forms import widgets
class UserForm(forms.Form):
    username = fields.CharField(
        required=True,
        error_messages={'required': '用户名不能为空'},
        widget=widgets.TextInput(attrs={'class':'form-control'})   # 生成什么HTML插件
    ) # 正则表达式,生成HTML标签
    password = fields.CharField(
        required=True,
        error_messages={'required': '密码不能为空'},
        widget=widgets.TextInput(attrs={'class': 'form-control'})
    ) # 正则表达式,生成HTML标签
    email = fields.EmailField(
        required=True,
        error_messages={'required': '邮箱不能为空','invalid': '邮箱格式错误'},
        widget=widgets.EmailInput(attrs={'class': 'form-control'})
    )   # 正则表达式,生成HTML标签

def add_user(request):
    if request.method == 'GET':
        obj = UserForm()
        return render(request,'add_user.html',{'obj': obj})
    else:
        # 获取用户提交的数据 request.POST
        # 数据和正则表达式进行验证
        # 1. 是否验证成功
        # 2. 成功：获取数据
        # 3. 失败：错误信息
        obj = UserForm(request.POST)
        # 1. 是否验证成功
        if obj.is_valid():
            # 2. 成功：获取数据
            print("验证通过",obj.cleaned_data)
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect('/users2')
        else:
            # 3. 失败：错误信息
            print("错误信息", obj.errors)
            # print("错误信息",obj.errors["email"][0])
            # print("错误信息",obj.errors["username"][0])
            # print("错误信息",obj.errors["password"][0])
        return render(request, 'add_user.html',{'obj': obj})


def edit_user(request,uid):
    if request.method == "GET":
        user = models.UserInfo.objects.filter(id=uid).first()
        obj = UserForm(initial={'username':user.username,'password': user.password,"email":user.email})
        return render(request,'edit_user.html',{"uid":uid,'obj':obj})
    else:
        obj = UserForm(data=request.POST)
        if obj.is_valid():
            models.UserInfo.objects.filter(id=uid).update(**obj.cleaned_data)
            return redirect('/users2')
        return render(request, 'edit_user.html', {"uid": uid, 'obj': obj})
