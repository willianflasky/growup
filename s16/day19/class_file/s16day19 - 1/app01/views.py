from django.shortcuts import render
import time
from django.views.decorators.cache import cache_page

# @cache_page(10)
def index(request):
    ctime = time.time()
    return render(request,'index.html',{'ctime': ctime})

# 缓存
def home(request):
    ctime = time.time()
    return render(request, 'index.html', {'ctime': ctime})


def test(request):
    from s16day19 import pizza_done
    pizza_done.send(sender='xxxxx', toppings=123, size=456)


    return render(request,'test.html',{'n1': 123,'n2': "root"})