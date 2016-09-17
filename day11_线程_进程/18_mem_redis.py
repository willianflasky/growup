#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import memcache

mc=memcache.Client(['192.168.1.1:11211'],debugy=True)
mc.set('foo','bar')
ret=mc.get('foo')
print(ret)


#天生集群
#基本操作
#gets,cas


import redis



