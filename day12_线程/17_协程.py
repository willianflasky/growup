#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

#利用一个线程,分解一个线程成为多个"微线程",程序级别实现.
#greenlet

#gevent对greenlet封装

from gevent import monkey;monkey.patch_all()
import gevent
import requests

def f(url):
    print("GET:%s"%url)
    resp=requests.get(url)
    data=resp.text
    print("%d bytes received from %s."%(len(data),url))


gevent.joinall([
    gevent.spawn(f,'https://www.baidu.com'),
    gevent.spawn(f,"https://www.python.org"),
    gevent.spawn(f,'https://www.apple.com')
])


"""
from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()
    print(34)
    gr2.switch()


def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()

"""
"""
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])

"""