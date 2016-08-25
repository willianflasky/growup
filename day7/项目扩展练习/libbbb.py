#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

from backend.commons import Foo



class MyFoo(Foo):
    def f1(self):
        print('before')
        super(MyFoo,self).f1()
        print('after')