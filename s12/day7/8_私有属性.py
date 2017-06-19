#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


class Foo():
    __cc=123
    def __init__(self,name):
        self.__name=name

    def f1(self):
        print(self.__name)

    #def f3(self):
    #    print(Foo.__cc)

    @staticmethod       #静态方法不需要创建对像
    def f3():
        print(Foo.__cc)


    def __f4(self):
        print(self.__name)


class Bar(Foo):
    def f2(self):
        print(self.__name)

obj=Foo('alex')
obj.f1()

#obj.f3()
#print(obj._Foo__name) #不建议使用.
#继承也访问不了私有属性
#私有只能类自己本身成员内部可以访问的原则!


#Foo.f3()
#obj._Foo__f4()