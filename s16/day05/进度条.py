#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

def show_progress(total):
    received_size = 0
    current_percent = 0
    while received_size < total:
        if int((received_size / total) * 100) > current_percent:
            print("#", end="", flush=True)
            current_percent = int((received_size / total) * 100)
        new_size = yield
        received_size += new_size

import time
p = show_progress(10000)
p.__next__()
for x in range(10000):
    time.sleep(0.01)
    try:
        p.send(x)
    except StopIteration as e:
        print('100%')
        break