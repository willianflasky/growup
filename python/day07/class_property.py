#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

class A:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


a = A("alex")
a.name
