#!/usr/bin/env python
# -*-coding:utf8-*-
__author__ = "willian"
import time


# def deco(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(end_time - start_time)
#     return wrapper
#
# def myfunc():
#     time.sleep(0.6)
#
# myfunc = deco(myfunc)
# myfunc()

def deco_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


def deco_2(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("from deco_2:")
    return wrapper

@deco_1
@deco_2
def myfunc(a, b):
    print("a + b =", a+b)
    time.sleep(0.6)

myfunc(10, 9)
