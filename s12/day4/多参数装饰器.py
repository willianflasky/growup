#!/usr/bin/env python

"""
def w1(main_func):
    def outer(request,kargs):
        print('before')
        main_func(request,kargs)
        print('after')
    return outer


@w1
def show():
    print('show')


#N个参数
def w3(func):
    def inner(*args,**kwargs):
        print('auth')
        return func(*args,**kwargs)
    return inner

@w3
def f3(arg1,arg2,arg3):
        print("f3 %s,%s,%s"%(arg1,arg2,arg3))

f3('tom','is','boy')


#一个函数被多个装饰器装饰
def w1(func):
    def inner(*args,**kwargs):
        print('w1')
        return func(*args,**kwargs)
    return inner

def w2(func):
    def inner(*args,**kwargs):
        print('w2')
        return func(*args,**kwargs)
    return inner

@w1
@w2
def f3(arg1,arg2,arg3):
        print("f3 %s,%s,%s"%(arg1,arg2,arg3))

f3('tom','is','boy')
"""
#通用装饰器
def Before(request,kargs):
    print('before')

def After(request,kargs):
    print('after')

def Filter(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):
            before_result = before_func(request,kargs)
            main_result = main_func(request,kargs)
            after_result = after_func(request,kargs)
        return wrapper
    return outer

@Filter(Before, After)
def Index(request,kargs):
    print('index')

Index('a','b')