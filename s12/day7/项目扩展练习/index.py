#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

from settings import *
import libbbb

def execute():
    #model=__import__(Path)
    cls=getattr(libbbb,ClassName)
    obj=cls()
    obj.f1()

if __name__ == '__main__':
    execute()
