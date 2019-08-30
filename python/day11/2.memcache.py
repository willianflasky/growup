#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


import memcache
import time

conn = memcache.Client(['192.168.11.75:12000'], cache_cas=True, debug=True)

conn.set('wb_num', 100)
v = conn.gets('wb_num')
print(v)

time.sleep(10)
conn.cas('wb_num', 95)
v = conn.get('wb_num')
print(v)


