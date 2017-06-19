#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

class Pager:
    def __init__(self,all_count):
        self.all_count=all_count

    @property
    def all_pager(self):
        a1,a2 = divmod(self.all_count,10)
        if a2 == 0:
            return a1
        else:
            return a1 + 1

    @all_pager.setter
    def all_pager(self,value):
        self.all_count=value


    @all_pager.deleter
    def all_pager(self):
        del self.all_count
        print('delete all_pager')


p=Pager(101)
ret=p.all_pager
print(ret)

#属性:
#不论不类的东西
#具有方法的写作形式,又有字段的访问形式.
"""

class Pager:
    def __init__(self,all_count):
        self.all_count=all_count

    def f1(self):
        return 123
    def f2(self,value):
        self.all_count=value
    def f3(self):
        return 456

    foo=property(fget=f1,fset=f2,fdel=f3)
#1
p=Pager(101)
ret=p.foo
print(ret)
#2
p.foo='alex'
#3
def p.foo

"""