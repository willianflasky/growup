#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import threading
import time


lock = threading.BoundedSemaphore(3)    # 可以一次进三个线程修改数据

v = 10


def task(arg):
    lock.acquire()
    time.sleep(2)
    global v
    v -= 1
    print(v)
    lock.release()


for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
