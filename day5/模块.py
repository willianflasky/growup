#!/usr/bin/env python3


import os,sys

#获取全部路径
print(os.path.abspath(__file__))
#获取目录
print(os.path.dirname(os.path.abspath(__file__)))
#获取文件名
print(os.path.basename(__file__))




import time,datetime

"""
print(time.clock())
print(time.process_time())
print(time.ctime(time.time()-86400))#昨天
print(time.gmtime())
print(time.localtime())
print(time.strftime("%Y-%m-%d_%H-%M-%S",time.gmtime(time.time()-86400)))#昨天
print(time.strptime("2016-05-02","%Y-%m-%d"))
"""
print(datetime.date.today())
print(datetime.datetime.now()- datetime.timedelta(days=10))

"""
#时间戳-->struct_time
print(time.time())
print(time.gmtime(time.time()))

#struct_time-->时间戳
print(time.localtime())
print(time.mktime(time.localtime()))

#字符串-->struct
print(time.strptime("20150505","%Y%m%d"))
#struct-->字符串
print(time.strftime("%Y%m%d",time.localtime()))

"""
