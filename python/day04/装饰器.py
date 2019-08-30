#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import time


def timer(func):
    def wrapper(*args, **kwargs):       # 接收万能传值
        start_time = time.time()
        res = func(*args, **kwargs)     # 接收万能传值
        end_time = time.time()
        print("run time is :", end_time - start_time)
        return res
    return wrapper


@timer
def index(msg):
    print("in the index", msg)
    return 1

ret = index("hello world!")
print(ret)


"""
重点:
    1.*args,**kwargs万能传值.
    2.返回值.
"""