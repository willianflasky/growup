#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


from threading import Timer


def hello():
    print('hello world!')

t = Timer(1,hello)
t.start()
