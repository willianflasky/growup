#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


from concurrent.futures import ProcessPoolExecutor


def task(arg):
    print(arg)
    return arg + 100


def call(arg):
    data = arg.result()
    print(data)


if __name__ == '__main__':
    pool = ProcessPoolExecutor(5)
    for i in range(10):
        obj = pool.submit(task, i)
        obj.add_done_callback(call)
