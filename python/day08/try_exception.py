#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


# try:
#     names = ['alex']
#     info[1:32]
#     info[5]
# except ValueError as e:
#     print(e)
#
# except IndexError as e:
#     print(e)
#
# except BaseException as e:
#     print('unknown error!', e)
#
#
# else:
#     print("什么都没有")
#
# finally:
#     print("无论有没有错, 都执行!")

import os

def getdirsize(dir):
   size = 0
   for root, dirs, files in os.walk(dir):
      size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
   return size

res = getdirsize('/Users/willian/Music')
print(res)