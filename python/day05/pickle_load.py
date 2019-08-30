#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import json as pickle

f = open('account.db', 'r')

data = pickle.load(f)
print(data)
f.close()

