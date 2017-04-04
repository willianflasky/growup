#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import time
import threading

lock = threading.Condition()


def task(arg):
    time.sleep(1)
    lock.acquire()
    lock.wait()
    print("线程:", arg)
    lock.release()


for i in range(10):
    t = threading.Thread(target=task, args=(i, ))
    t.start()

while True:
    value = input(">>>")
    lock.acquire()
    lock.notify(int(value))
    lock.release()
