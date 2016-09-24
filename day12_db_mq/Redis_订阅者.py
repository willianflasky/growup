#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


import RedisHelper



obj=RedisHelper.RedisHelper()
data=obj.subscribe('fm111.7')
print(data.parse_response())

