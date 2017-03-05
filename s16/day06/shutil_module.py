#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import shutil
# http://www.cnblogs.com/wupeiqi/articles/4963027.html

# copy fileobj
# f1 = open('access.log')
# f2 = open("access1.log", 'w')
# shutil.copyfileobj(f1, f2, length=1024)

# copy file
# shutil.copyfile('access.log', 'access2.log')

# 仅拷贝权限。内容、组、用户均不变
# shutil.copymode()

# 拷贝状态的信息，包括：mode bits, atime, mtime, flags. 内容不变
# shutil.copystat()

# copy 目录
# copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))

