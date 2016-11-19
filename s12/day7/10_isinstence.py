#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


#isinstance #查看对象是不是由某个类创建的.
#issubclass #查看某个类是不是另外一个子类.

class Bar(Foo):
    pass


class Foo(Bar):
    pass
obj1=Foo()
ret=isinstance(obj1,Bar)
print(ret)

ret=issubclass(Bar,Foo)s
print(ret)


"""
class C1:
    def f1(self):
        print('c1.f1')

class C2(C1):
    def f1(self):
        #super(C2,self).f1()
        C1.f1(self)
        print('c2.f1')

obj=C2()
obj.f1()
"""