#!/usr/bin/env python

"""
#一个参数
def w1(func):   #func = f1
    def inner(arg):     #arg是f1的参数
        print('auth %s'%arg)    #新增加内容
        return func(arg)        #运行老f1
    return inner                #返回inner给新的f1

@w1
def f1(arg):
    print('f1   %s'%arg)

f1('alex')          #运行新的F1了

#二个参数

def w2(func):
    def inner(arg1,arg2):
        print("auth %s,%s"%(arg1,arg2))
        return func(arg1,arg2)
    return inner

@w2
def f2(arg1,arg2):
    print("f2  %s,%s"%(arg1,arg2))

f2('tom','boy')


"""