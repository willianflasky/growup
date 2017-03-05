#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


class People(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender= gender

    def test(self):
        print("from People test")


class Teacher(People):
    def __init__(self, name, age, gender, level):
        People.__init__(self, name, age, gender)  # 这里的self是上一行self,上一行的self,实例t. 这里直接从people中调用__init__函数,需要手动写self参数.
        # super().__init__(name, age, gender)
        self.level = level


t = Teacher('alex', 18, 'man', "高级讲师")
print(t.level)
