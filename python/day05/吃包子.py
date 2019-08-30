#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import time


def consumer(name):
    print("{0}准备吃包子了".format(name))
    while True:
        baozi = yield
        print("包子来了[%s],被[%s]吃了" % (baozi, name))


def producer():
    c1 = consumer("tom")
    c2 = consumer("eric")
    c1.__next__()           # 让c1停在 baozi = yield
    c2.__next__()           # 让c2停在 baozi = yield
    print("老子开始准备做包子!")
    for i in range(1, 10):
        time.sleep(1)
        c1.send(i)          # send:1.唤醒yield.   2.发送包了i给yield(传值给yield)
        c2.send(i)

producer()

