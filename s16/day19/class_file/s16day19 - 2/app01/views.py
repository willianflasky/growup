from django.shortcuts import render,HttpResponse
import time
from app01 import models
from utils import BaseReponse

def index(request):
    # models.UserInfo.objects.create(username='u1',pwd='123123')
    # models.UserInfo.objects.create(username='u2',pwd='123123')
    user_list = models.UserInfo.objects.all()

    return render(request,'index.html',{'user_list': user_list})

def show(request):
    return render(request, 'show.html')



def get_data(request):
    # user_list = models.UserInfo.objects.all()
    # 1. 找模板渲染之后，生成字符串
    # return render(request,'tpl.html',{'user_list': user_list})
    # user_list = [
    #     {'id':1,'name':'xx','pwd': 123},
    #     {'id':1,'name':'xx','pwd': 123},
    #     {'id':1,'name':'xx','pwd': 123},
    #     {'id':1,'name':'xx','pwd': 123},
    # ]
    # Models获取数据时，序列化方式一
    # from django.core import serializers
    # user_list = models.UserInfo.objects.all()
    # data = serializers.serialize("json", user_list)
    # return HttpResponse(data)
    # Models获取数据时，序列化方式二
    # user_list = models.UserInfo.objects.values('id','username')
    # user_list = list(user_list)
    # import json
    # return HttpResponse(json.dumps(user_list))
    # Models获取数据时，序列化方式三
    # user_list = models.UserInfo.objects.values_list('id', 'username')
    # user_list = list(user_list)
    # import json
    # return HttpResponse(json.dumps(user_list))
    import json
    ret = BaseReponse()
    try:
        user_list = models.UserInfo.objects.values('id','urname')
        user_list = list(user_list)
        ret.status = True
        ret.data = user_list
    except Exception as e:
        ret.error = "获取数据失败"
    data = json.dumps(ret.__dict__)
    return HttpResponse(data)

# 缓存
def home(request):
    ctime = time.time()
    return render(request, 'index.html', {'ctime': ctime})


def test(request):
    # from s16day19 import pizza_done
    # pizza_done.send(sender='xxxxx', toppings=123, size=456)

    return render(request,'test.html',{'n1': 123,'n2': "root"})