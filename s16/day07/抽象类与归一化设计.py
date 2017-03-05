#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import abc


class AllFile(metaclass=abc.ABCMeta):

    def test(self):
        print("testing")

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass


class Text(AllFile):

    def read(self):
        pass

    def write(self):
        pass


t = Text()
t.test()