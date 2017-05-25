from django.shortcuts import render, HttpResponse, redirect
from host.models import *
from functools import wraps
import json
# Create your views here.


def auth(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        username = request.session.get('user', "")
        if username:
            return func(request, username, **kwargs)
        else:
            return redirect('/')
    return wrapper


def logout(request):
    request.session.clear()
    return redirect("/")


def login(request):
    username = request.session.get('user', "")
    if username:
        return redirect("/host/")

    if request.method == 'POST':
        user = request.POST.get('user')
        passwd = request.POST.get('passwd')
        obj = Users.objects.filter(username=user, password=passwd).first()
        res = {'status': True, 'error': None}
        if obj:
            request.session['user'] = user
            request.session['passwd'] = passwd
            return HttpResponse(json.dumps(res))
        else:
            res['status'] = False
            res['error'] = "用户名或者密码错误"
            return HttpResponse(json.dumps(res))

    elif request.method == 'GET':
        return render(request, 'login1.html', locals())


@auth
def host(request, *args, **kwargs):
    res = {'status': True, "error": "OK"}

    username = args[0]
    uid = Users.objects.filter(username=username).values('id')[0]
    host_list = Users.objects.filter(id=uid['id']).values('hosts__id', 'hosts__ip', 'hosts__port', 'hosts__hostuser',
                                                          'hosts__bussiness__bussline')

    if request.method == 'POST':
        flag = request.GET.get('f')
        if flag == 'delete':
            nid = request.POST.get('nid')
            Hosts.objects.filter(id=nid).delete()
            return HttpResponse(json.dumps(res))

        elif flag == 'edit':
            nid = int(request.POST.get('nid'))
            ip = request.POST.get('ip')
            port = request.POST.get('port')
            user = request.POST.get('user')
            buss = (request.POST.get('buss'))
            buss_obj = Bussiness.objects.filter(bussline=buss)[0]
            h = Hosts.objects.filter(id=nid)[0]
            if h.ip == ip and h.port == port and h.hostuser == user and h.bussiness.bussline == buss:
                res['status'] = False
                res['error'] = "数据没有变化"
                return HttpResponse(json.dumps(res))
            else:
                Hosts.objects.filter(id=nid).update(ip=ip, port=port, hostuser=user, bussiness=buss_obj)
                return HttpResponse(json.dumps(res))

        elif flag == 'add':
            pass

    return render(request, 'host.html', locals())


@auth
def edit(request, *args, **kwargs):
    username = args[0]
    res = {'status': True, "error": "OK"}
    all_line = Bussiness.objects.values('bussline')
    if request.GET.get('line') == "1":
        new_line = request.POST.get('new_line')
        if len(new_line) == 0:
            res['status'] = False
            res['error'] = "不能提交空值"
            return HttpResponse(json.dumps(res))
        result = Bussiness.objects.filter(bussline=new_line).count()
        if not result:
            Bussiness.objects.create(bussline=new_line)
            return HttpResponse(json.dumps(res))
        else:
            res['status'] = False
            res['error'] = "新业务线已经存在"
            return HttpResponse(json.dumps(res))

    elif request.GET.get('line') == "2":
        ip = request.POST.get('ip')
        port = request.POST.get('port')
        hostuser = request.POST.get('hostuser')
        hostpass = request.POST.get('hostpass')
        s1 = request.POST.get('s1')

        if len(ip) == 0 or len(port) == 0 or len(hostuser) == 0 or len(hostpass) == 0 or len(s1) == 0:
            res['status'] = False
            res['error'] = "全部为必填项"
            return HttpResponse(json.dumps(res))
        else:
            buss_id = Bussiness.objects.filter(bussline=s1).values('id')[0]
            if buss_id:
                Hosts.objects.create(ip=ip, port=port, hostuser=hostuser, hostpass=hostpass, bussiness_id=buss_id['id'])
                return HttpResponse(json.dumps(res))
    elif request.GET.get('line') == '3':
        ip = request.POST.get('ip')
        user = request.POST.get('user')
        ip_obj = Hosts.objects.filter(ip=ip)
        user_obj = Users.objects.filter(username=user)
        if ip_obj and user_obj:
            ip_obj[0].user.add(user_obj[0])
            return HttpResponse(json.dumps(res))
        else:
            res['status'] = False
            res['error'] = "没有找到主机地址或者用户名."
            return HttpResponse(json.dumps(res))
    return render(request, 'edit.html', locals())
