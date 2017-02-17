#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import sys,os
sys.path.append('/Users/willian/PycharmProjects/growup/s16/day04')


ret = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir))
print(ret)
from glance.api import policy

policy.get()