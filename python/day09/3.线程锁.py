#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


import threading
import time


# lock = threading.Lock()   # 只能上一次锁,只会解一次锁
lock = threading.RLock()    # 支持上多个锁

v = 10


def task(arg):
    time.sleep(2)
    lock.acquire()
    global v
    v -= 1
    print(v)
    lock.release()


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
