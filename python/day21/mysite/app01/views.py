from django.shortcuts import render, HttpResponse

# Create your views here.
from app01 import tasks


def task_test(request):
    a = int(request.GET.get('a'))
    b = int(request.GET.get('b'))

    res = tasks.add.delay(a, b)
    print("start running task")
    print("async task res", res.get())
    return HttpResponse('res %s' % res.get())
