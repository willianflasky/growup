#!/usr/bin/env python
#coding:utf8

class Foo:
    cc=123  #静态字段(保存在类中)
    def __init__(self):
        self.name='alex' #普通字段(保存在对象中)

    def show(self): #普通方法,由对象调用执行,属于类.
        print(self.name)




#一般情况自己访问自己的字段
#规则:
# 对象中的字段只能用对象访问,
# 静态字段要用类去访问,(万不得已可以使用对象访问)

class Province:
    country='中国'

    def __init__(self,name):
        self.name=name

hn=Province('河南')
print(Province.country)
print(hn.name)


