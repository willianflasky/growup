#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/30 下午7:30
__author__ = "willian"

from snow import Snow
from snow import HttpResponse
from snow import Future

request_list = []


def callback(request, future):
    return HttpResponse(future.value)


def req(request):
    obj = Future(callback=callback)
    request_list.append(obj)
    yield obj


def stop(request):
    obj = request_list[0]
    del request_list[0]
    obj.set_result('done')
    return HttpResponse('stop')


routes = [
    (r'/req/', req),
    (r'/stop/', stop),
]

app = Snow(routes)
app.run(port=8012)
