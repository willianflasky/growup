#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from collections import Iterable

print(isinstance([], Iterable))


"""
    1.生成器:可以被for循环. [],{},(),                   generator
    2.迭代器:不但可以被for循环,还可以next.   yield        Iterator
"""