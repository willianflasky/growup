#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


from greenlet import greenlet


# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
#
# def test2():
#     print(56)
#     gr1.switch()
#     print(78)
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()

from gevent import monkey;monkey.patch_all()
import gevent
import requests


def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    print('%s bytes received from %s' % (resp.status_code, url))

gevent.joinall([
        gevent.spawn(f, 'http://www.baidu.com/'),
        gevent.spawn(f, 'http://www.sina.com.cn/'),
])
