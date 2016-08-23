#!/usr/bin/env python
#coding:utf8


class Provence:
    cc=123  #静态字段(保存在类中)
    def __init__(self):
        self.name='alex' #普通字段(保存在对象中)

    def show(self): #普通方法,由对象调用执行,属于类.
        print()

    @staticmethod
    def f1(arg1,arg2):
        print(arg1,arg2)


    @classmethod
    def f2(cls):
        print(cls)

    def f3(self):
        return self.name[1]

#普通方法变成静态方法1.去掉self.2.@staticmethod
#静态方法属于类,由类来调用.
#为了节省内存,不需要创建对象就可以调用方法.


#方法
#普通方法:至少一个SELF,对象执行
#静态方法:任意参数,不需SELF,类执行(可以用对象执行,但是不建议)
#类方法:至少一个cls,类执行(可以用对象执行,但是不建议,相当于Provence.f2(Provence))

obj=Provence()
obj.f1(1,2)