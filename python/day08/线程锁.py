#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import threading
import time

gl_num = 0


def show(arg):
    global gl_num
    time.sleep(1)
    gl_num += 1
    print(gl_num)

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print('main thread stop')

# gl_num = 0
#
# lock = threading.RLock()
#
#
# def func():
#     lock.acquire()
#     global gl_num
#     gl_num += 1
#     time.sleep(1)
#     print(gl_num)
#     lock.release()
#
# for i in range(10):
#     t = threading.Thread(target=func)
#     t.start()
#
# print('main thread stop')
