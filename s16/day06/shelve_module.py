#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import shelve

# 基于pickle模块,

d = shelve.open('shelve_test')


class Test(object):
    def __init__(self, n):
        self.n = n

t1 = Test(123)
t2 = Test(456)
name = ['alex', 'rain', 'test']
d['test'] = name
d['t1'] = t1
d['t2'] = t2

d.close()
