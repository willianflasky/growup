#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


import memcache

conn = memcache.Client(['192.168.11.75:12000'], cache_cas=True, debug=True)

v = conn.gets('wb_num')
print(v)
conn.cas('wb_num', 99)
v = conn.gets('wb_num')
print(v)
