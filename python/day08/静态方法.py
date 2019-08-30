#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

"""
@classmethod
    类方法,属于类,只能访问类变量,不能访问实例的变量.

@staticmethod
　　不属于类和实例,只是名义上的归属.它不能访问类和实例的变量，只能处理自己的传值。定义方法时不需要写self.

@property
    把一个方法变成静态属性(变量属性)

"""


class foo(object):
    ab = "abababa"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def test(cls):
        print(cls.ab)

f = foo('alex', 22)
f.test()
