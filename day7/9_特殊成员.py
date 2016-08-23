#!/usr/bin/env python
#coding:utf8
#Author: willianflasky





class Foo:
    """this test"""

    def __init__(self,name,age):    #构造方法,obj=Foo('tom')时运行
        self.name=name
        self.age=age

    def __del__(self):          #析构方法,删除时息动运行
        print('del done')

    def __call__(self):         #p() #对象后面加括号就是执行call方法,#Foo()() #这样也可以执行call方法
        print('call')

    def __str__(self):          #1.obj1=('tom');print(obj1)则执行__str__.  2.str(obj1)也可以执行,没有这个方法是不可以的.
        return self.name

    def __add__(self, other):   #两个对象相加
        temp="%s --> %d" %(self.name,other.age)
        return temp

    def __getitem__(self, item):   #obj1['item']
        #print(item.start)
        #print(item.stop)
        #print(item.step)
        print(type(item))
        return 123

    def __setitem__(self, key, value):  #obj1['alex']=73
        #print('setitem:%s %s'%(key,value))
        print(type(key),type(value))
        print(key,value)


    def __delitem__(self, key):         #del obj1['k1']
        print(type(key))



"""
p=Foo()
print(p.__doc__)
print(p.__module__)
print(p.__class__)
ret=obj1+obj2
print(ret)
ret=obj1.__dict__   #获取对象中封装的数据.
print(Foo.__dict__) #获取类中的成员
#
ret=obj1[1:4:3]
obj1[1:4:3]=[11,22,33]
del obj1[1:4]
"""

obj1=Foo('alex',73)

"""
class bar(object):
    def __iter__(self):
        return iter([11,22,33])
        #yield 1
        #yield 1
b=bar()

for i in b:
    print(i)

"""
