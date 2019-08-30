from django.shortcuts import render, HttpResponse, redirect
from app01.models import *

# Create your views here.

from django.views import View


class User(View):
    def dispatch(self, request, *args, **kwargs):
        print("before")
        obj = super(User, self).dispatch(request, *args, **kwargs)
        print("after")
        return obj

    def get(self, request):
        print("get...")
        return HttpResponse("....")

    def post(self, request):
        print("POST")
        return HttpResponse("....")


def test(request):
    # ret = UserInfo.objects.all().values("id", "username", "password", "dp__title")
    # for row in ret:
    #     print(row['id'], row['username'], row['password'], row['dp__title'])

    # ret = UserInfo.objects.values_list("id", "username", "password", "dp__title")
    # for row in ret:
    #     print(row[0], row[1], row[2], row[3])
    # v = DePart.objects.all()
    # for row in v:
    #     print(row.id, row.title, row.userinfo_set[0])
    obj = UserGroup.objects.filter(id=3).first()
    # obj.m.add(1,2,3)
    # obj.m.add(1,2,3)
    # obj.m.add(*[1, 2, 3])
    # obj.m.remove(1)
    # obj.m.remove(1,2,3)
    # obj.m.remove(*[1,2,3])
    # obj.m.clear()

    # obj.m.set([1,2,3])  # 其它的删除,只剩下1,2,3
    # obj.m.filter(id__gt=3)    # 第二次过滤,过滤 userinfo的表.

    return HttpResponse("...")


def home(request):
    # v = request.COOKIES.get('uuu')
    v = request.session.get('user')
    if v:
        return render(request, 'home.html', locals())
    else:
        return redirect('/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'msg': ''})
    else:
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        ct = UserInfo.objects.filter(username=u, password=p).count()
        if ct:
            obj = redirect('/home/')
            # 方法一写cookie
            # obj.set_cookie('uuu', u, 30)
            # 方法二写session
            # 生成随机字符串
            # 发送给客户端
            # 保存服务器
            request.session['user'] = u
            request.session['pass'] = p
            return obj
        else:
            return render(request, 'login.html', {'msg': "用户名或者密码错误!"})


def logout(request):
    request.session.clear()
    return redirect('/login/')


def ajax(request):
    if request.method == 'GET':
        return render(request, 'ajax.html')
    elif request.method == 'POST':
        user = request.POST.get('uuu')
        pwd = request.POST.get('ppp')
        obj = UserInfo.objects.filter(username=user,password=pwd).first()
        ret = {'status': True, 'error': None}
        import json
        if obj:
            request.session['user'] = user
            request.session['pwd'] = pwd
            return HttpResponse(json.dumps(ret))  # 后端不能跳转,只能交给AJAX跳转

        else:
            ret['status'] = False
            ret['error'] = "用户名或者密码错误"
            return HttpResponse(json.dumps(ret))

