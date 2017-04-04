#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from multiprocessing import Process, Manager


def task(num, li):
    li.append(num)
    print(li)

if __name__ == '__main__':
    # v = Manager().dict()
    v = Manager().list()
    for i in range(10):
        p = Process(target=task, args=(i, v))
        p.start()
    input(">>")