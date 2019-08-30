#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


import nb_thread


def f1(future):
    response = future.result()
    print(len(response.text))


def f2(future):
    response = future.result()
    print(len(response.text))


def f3(future):
    response = future.result()
    print(len(response.text))

url_list =[
    {'url': 'http://www.baidu.com', 'call': f1},
    {'url': 'http://www.qq.com', 'call': f2},
    {'url': 'http://www.sina.com', 'call': f3},
]

nb_thread.run(url_list)

