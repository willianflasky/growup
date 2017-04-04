#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from multiprocessing import Process
import time


def task(arg):
    time.sleep(arg)
    print(arg)

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=task, args=(i, ))
        p.daemon = True  # default false,如果是True时,主进程不等子进程.
        p.start()
        p.join(1)   # 串行了,主进程只等待子进程1秒.

    print("主进程结束了!")
