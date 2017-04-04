#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

#
# def init(self, name, age):
#     self.name = name
#     self.age = age
#
#
# def sayhi(self):
#     print("hello", self.name)
#
#
# Test = type('Test', (object,), {'sayhi': sayhi, "__init__": init})
#
# t1 = Test('alex', 22)
# t1.sayhi()


# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#         print("foo__init__")
#
#     def __new__(cls, *args, **kwargs):
#         print("foo __new__", *args, **kwargs)
#         obj = object.__new__(cls)
#         print("obj:", obj)
#         return obj
#
# f = Foo('alex')
# # print(f)
# # print(f.name)


class MyType(type):
    def __init__(self, *args, **kwargs):    # self == obj传过来的,又是foo类.
        print("MyType: __init__", self, *args, **kwargs)  # self == obj == foo

    def __call__(self, *args, **kwargs):    # self == foo
        print("MyType: __call__", self, *args, **kwargs)
        obj = self.__new__(self)    # 开内存 ,foo没有__new__,所以继承父类MyType的__new__
        self.__init__(obj, *args, **kwargs)  # foo的__init__
        obj.age = 22
        return obj   # return给f

    def __new__(cls, *args, **kwargs):
        print("MyType __new__", cls, *args, **kwargs)    # 第一步: cls 是mytype类本身
        obj = type.__new__(cls, *args, **kwargs)         # 第二步: 生成Foo内存地址
        return obj                                       # 第三步: 实例return给上面的__init__


class Foo(object, metaclass=MyType):
    def __init__(self, name):
        self.name = name
        print("foo __init__")

    def __call__(self, *args, **kwargs):
        print("call ... ")

f = Foo('alex')

"""
    type--(实例化)-->MyType--(实例化)-->Foo--(实例化)-->f

一.当不执行 f = Foo('alex')
    1.type自动实例化一个MyType
    2.MyType通过type的__new__生成Foo的内存地址.
    3.把Foo这个实例return给MyType __init__(self),self等于obj就是foo类.

二.当执行 f = Foo('alex')
    1.当Foo()后面增加了这对括号时,就调用了MyType的__call__
    2.开辟内存 ,foo没有__new__,所以继承父类的__new__,然后执行.
    3.将这个块内存return给f.

"""