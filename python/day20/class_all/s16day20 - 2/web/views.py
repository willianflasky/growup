import json
from django.shortcuts import render,HttpResponse
from repository import models
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
    ret = {'status': False, 'error': ''}
    if request.session.get('is_login'):
        pass
    else:
        return HttpResponse(json.dumps(ret))

