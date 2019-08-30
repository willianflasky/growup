#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/1/16 下午3:50
__author__ = "willian"

from werkzeug.wrappers import Response, Request
from werkzeug.serving import run_simple


@Request.application
def hello(request):
    return Response('hello world')


if __name__ == '__main__':
    run_simple('localhost', 4000, hello)
