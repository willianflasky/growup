from django.shortcuts import render, HttpResponse, redirect
from repository.models import *
import json
# Create your views here.


def index(request):
    news_list = News.objects.all()
    for row in news_list:
        print(row.title, row.favor_users.count())
    return render(request, 'index.html', locals())


def do_favor(request):
    """
    1. 获取新闻ID
    2. 当前登录的用户ID
    3. 在favor表中插入数据
    4. 新闻表中的favor_count + 1
    :param request:
    :return:
    """

    ret = {'status': 0, 'error': ''}
    if request.session.get('is_login'):
        news_id = request.GET.get('nid')
        current_user_id = request.session['user_info']['user_id']
        ct = Favor.objects.filter(user_info_id=current_user_id,news_id=news_id).count()
        if ct:
            Favor.objects.filter(user_info_id=current_user_id, news_id=news_id).delete()
            news_obj = News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count - 1
            News.objects.filter(nid=news_id).update(favor_count=temp)
            ret['status'] = 1
        else:
            Favor.objects.create(user_info_id=current_user_id,news_id=news_id)
            news_obj = News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count + 1
            News.objects.filter(nid=news_id).update(favor_count=temp)
            ret['status'] = 2
    return HttpResponse(json.dumps(ret))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # code = request.POST.get('code')
        # if code.upper() == request.session['check_code'].upper():
        obj = UserInfo.objects.filter(username=request.POST.get('username'), password=request.POST.get('password')).first()
        if obj:
            request.session['is_login'] = True
            request.session['user_info'] = {'user_id': obj.nid, 'user_name': obj.username}
            return redirect('/index/')
        else:
            return render(request, 'login.html')
        # else:
        #     return render(request, 'login.html')
