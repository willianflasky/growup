import json
from django.shortcuts import render,HttpResponse,redirect
from repository import models
from utils import check_code as ac
from io import BytesIO


def index(request):
    news_list = models.News.objects.all()
    return render(request,'index.html',{'news_list': news_list})

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
        ct = models.Favor.objects.filter(user_info_id=current_user_id,news_id=news_id).count()
        if ct:
            models.Favor.objects.filter(user_info_id=current_user_id, news_id=news_id).delete()
            news_obj = models.News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count - 1
            models.News.objects.filter(nid=news_id).update(favor_count=temp)
            ret['status'] = 1
        else:
            models.Favor.objects.create(user_info_id=current_user_id,news_id=news_id)
            news_obj = models.News.objects.filter(nid=news_id).first()
            temp = news_obj.favor_count + 1
            models.News.objects.filter(nid=news_id).update(favor_count=temp)
            ret['status'] = 2
    return HttpResponse(json.dumps(ret))

def login(request):

    if request.method == 'GET':
        return render(request,'login.html')
    else:
        code = request.POST.get('code')
        if code.upper() == request.session['check_code'].upper():
            obj = models.UserInfo.objects.filter(username=request.POST.get('username'),password=request.POST.get('password')).first()
            if obj:
                request.session['is_login'] = True
                request.session['user_info'] = {'user_id': obj.nid,'user_name': obj.username}
                return redirect('/index/')
            else:
                return render(request, 'login.html')
        else:
            print('验证码错误')
            return render(request, 'login.html')


def check_code(request):
    # {  # 后台生成图片，并在图片上写文字#}
    # 自己写一个空白图片
    # 在图片上写文字
    img_obj, code = ac.create_validate_code()
    stream = BytesIO()
    img_obj.save(stream,'png')
    request.session['check_code'] = code
    return HttpResponse(stream.getvalue())


