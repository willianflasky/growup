#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
#
# r1 = requests.get('http://127.0.0.1:8000/login/')
#
# r2 = requests.post(
#     url='http://127.0.0.1:8000/login/',
#       data={
#           'csrfmiddlewaretoken': "31tFZX2IZ0blOTfZ5VmfXDMLuvYaTaSjajVCiAWje07nuPLRJa6DvsXIRyzczXBh",
#           'username': 'alex',
#           'password': '123',
#           'code': "sidfjsd"
#
#       }
# )
# print(r2.text)


### 1、首先登陆任何页面，获取cookie

i1 = requests.get(url="http://dig.chouti.com/help/service")

### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
i2 = requests.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': "8615131255089",
        'password': "woshiniba",
        'oneMonth': ""
    },
    cookies=i1.cookies.get_dict()
)

### 3、点赞（只需要携带已经被授权的gpsd即可）
gpsd = i1.cookies.get_dict()['gpsd']
i3 = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=12439696",
    cookies={'gpsd': gpsd}
)
print(i3.text)