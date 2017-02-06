#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


def main(name):
    print("my name is {0}".format(name))

# main('alex')


# 实参:所有的数据类型都可以被当作参数传给函数.
# 行参:仅在函数内部有效,函数结束后释放.(形参的作用域只在当前函数内有效).


# def f1():
#     global n
#     n = "change it"
#     print(n)
#
# n = "test"
# print(n)
# f1()
# print(n)


# 函数内可以修改字典,列表,集合,实例.是为列表的内存地址没有,只是修改里面的元素.
# def change():
#     print(name)
#     name[0] = 'Mack'
#     name.append('tom')
#     info['age'] = 22
#     # info = {} 这样则就报错,不允许了.
#
# name = ['alex', 'jack']
# info = {'name': 'rain'}
#
# change()
# print(name, info)


# *args **kwargs
# def f2(name, age, *args, **kwargs):
#     print("name", name)
#     print("age", age)
#     # print("args", args)
#     # print("kwarges", kwargs)
#     for i in kwargs.keys():
#         print(i, kwargs[i])
#
#
# f2('alex', 22, 'tom', 'eric', addr='昌平公主', ip='顺义王子')
#
#

# 递归, 一层层进入,一层层退出.

