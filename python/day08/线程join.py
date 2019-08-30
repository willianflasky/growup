#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


import threading
import time


def sayhi(num):     # 定义每个线程要运行的函数
    print("running on number:%s" % num)
    time.sleep(3)


if __name__ == '__main__':
    thread_list = []
    for i in range(10):
        t1 = threading.Thread(target=sayhi, args=(i,))
        t1.start()
        thread_list.append(t1)

    for x in thread_list:
        x.join()

    print("master thread------")

