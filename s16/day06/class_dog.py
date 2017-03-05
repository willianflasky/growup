#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


class Dog(object):
    age = 22

    def __init__(self, name, type1, sex):
        self.name = name
        self.type = type1
        self.__sex = sex

    def balk(self):
        print("{0} wang wang!".format(self.name))

    def eat(self, food):
        print("{0} eating {1}".format(self.name, food))

    def get_sex(self):
        print(self.__sex)

d = Dog('杨帅', '京巴', 'F')
d.get_sex()
# print(d._Dog__sex)
# print(d.name, d.type)
# d.balk()
# d.eat("包子")

