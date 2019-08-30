#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from gevent import monkey; monkey.patch_all()

import gevent
import requests


def f(url):
    response = requests.get(url)
    print(response.url, response.status_code)


gevent.joinall([
    gevent.spawn(f, 'http://www.baidu.com'),
    gevent.spawn(f, 'http://www.qq.com')
])
