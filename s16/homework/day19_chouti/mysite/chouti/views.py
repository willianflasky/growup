from django.shortcuts import render, HttpResponse, redirect
from utils.formtable import *
# Create your views here.
from utils.status import BaseReponse
from chouti.models import *
import json
from utils.page import PageInfo
import datetime
import time


def index(request):
    all_count = News.objects.all().count()
    page_info = PageInfo(request.GET.get('p'), 6, all_count, request.path_info, page_range=3)
    objs = News.objects.all().order_by('-id').prefetch_related('user', 'favor')[page_info.start():page_info.end()]

    # process time
    now = time.time()
    for obj in objs:
        obj.ctime = int(now - time.mktime(obj.ctime.timetuple()))
        obj.ctime = "%s分钟以前" % (int(obj.ctime/60))

    return render(request, 'index.html', locals())


def publish(request):
    print(request.POST)
    response = BaseReponse()
    return HttpResponse(json.dumps(response.__dict__, ensure_ascii=False))


def upload_image(request):
    import os
    response = BaseReponse()
    try:
        obj = request.FILES.get('img')
        file_path = os.path.join('static/images', obj.name)
        f = open(file_path, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        response.status = True
        response.data = file_path
    except Exception as e:
        response.status = False
    return HttpResponse(json.dumps(response.__dict__, ensure_ascii=False))


def favor(request):
    response = BaseReponse()
    obj = UserInfo.objects.filter(f__id=int(request.POST.get('nid')), username=request.session.get('user')).prefetch_related('f')
    if obj.count():
        user_obj = UserInfo.objects.filter(username=request.session.get('user'))[0]
        new_obj = News.objects.filter(id=int(request.POST.get('nid')))[0]
        new_obj.favor.remove(user_obj)
        response.status = True
        response.code = 2302
    else:
        user_obj = UserInfo.objects.filter(username=request.session.get('user'))[0]
        new_obj = News.objects.filter(id=int(request.POST.get('nid')))[0]
        new_obj.favor.add(user_obj)
        response.status = True
        response.code = 2301
    return HttpResponse(json.dumps(response.__dict__, ensure_ascii=False))


def logout(request):
    request.session.clear()
    return redirect('/')


def login(request):
    response = BaseReponse()
    try:
        obj = LoginForm(request.POST)
        if obj.is_valid():
            v = UserInfo.objects.filter(username=obj.cleaned_data['user'], password=obj.cleaned_data['pwd']).count()
            if v:
                response.status = True
                request.session['user'] = obj.cleaned_data['user']
            else:
                response.status = False
                response.message = 1
        else:
            response.status = False
            response.message = obj.errors
    except Exception as e:
        response.status = False

    return HttpResponse(json.dumps(response.__dict__, ensure_ascii=False))


def qu(request):
    all_count = News.objects.filter(zone=1).count()
    page_info = PageInfo(request.GET.get('p'), 6, all_count, request.path_info, page_range=3)
    objs = News.objects.filter(zone=1).order_by('-id').prefetch_related('user', 'favor')[page_info.start():page_info.end()]
    now = datetime.datetime.now()
    for obj in objs:
        obj.ctime = now - obj.ctime

    return render(request, 'qu.html', locals())


def dz(request):
    all_count = News.objects.filter(zone=2).count()
    page_info = PageInfo(request.GET.get('p'), 6, all_count, request.path_info, page_range=3)
    objs = News.objects.filter(zone=2).order_by('-id').prefetch_related('user', 'favor')[page_info.start():page_info.end()]
    now = datetime.datetime.now()
    for obj in objs:
        obj.ctime = now - obj.ctime

    return render(request, 'dz.html', locals())


def tp(request):
    all_count = News.objects.filter(zone=3).count()
    page_info = PageInfo(request.GET.get('p'), 6, all_count, request.path_info, page_range=3)
    objs = News.objects.filter(zone=3).order_by('-id').prefetch_related('user', 'favor')[page_info.start():page_info.end()]
    now = datetime.datetime.now()
    for obj in objs:
        obj.ctime = now - obj.ctime

    return render(request, 'tp.html', locals())


def at(request):
    all_count = News.objects.filter(zone=4).count()
    page_info = PageInfo(request.GET.get('p'), 6, all_count, request.path_info, page_range=3)
    objs = News.objects.filter(zone=4).order_by('-id').prefetch_related('user', 'favor')[page_info.start():page_info.end()]
    now = datetime.datetime.now()
    for obj in objs:
        obj.ctime = now - obj.ctime

    return render(request, 'at.html', locals())


def nw(request):
    all_count = News.objects.filter(zone=5).count()
    page_info = PageInfo(request.GET.get('p'), 6, all_count, request.path_info, page_range=3)
    objs = News.objects.filter(zone=5).order_by('-id').prefetch_related('user', 'favor')[page_info.start():page_info.end()]
    now = datetime.datetime.now()
    for obj in objs:
        obj.ctime = now - obj.ctime

    return render(request, 'nw.html', locals())