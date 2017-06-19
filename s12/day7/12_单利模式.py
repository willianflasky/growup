#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

class Foo:
    instance=None
    def __init__(self,name):
        self.name=name

    @classmethod
    def get_instance(cls):
        if cls.instance:
            return cls.instance
        else:
            obj=cls('alex')
            cls.instance=obj
            return obj



obj1=Foo.get_instance()
obj2=Foo.get_instance()

print(obj1)
print(obj2)
