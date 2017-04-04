#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
from multiprocessing import Process, Array


def task(num, li):
    li[num] = 1
    print(list(li))


if __name__ == '__main__':
    v = Array('i', 10)
    for i in range(10):
        p = Process(target=task, args=(i, v,))
        p.start()


