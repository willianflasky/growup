#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import json as pickle

accounts = {
    'id': 1234,
    "credit": 15000,
    'balance': 8000,
    'expire_date': "2020-5-1",
    "password": 123456,
}

f = open('account.db', 'w')

# f.write(pickle.dumps(accounts))  # 进内存了.依靠f.write写文件.
pickle.dump(accounts, f)           # 直接写文件.
f.close()
