#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import threading
import time


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s" % n)
    semaphore.release()


if __name__ == '__main__':

    num = 0
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()
