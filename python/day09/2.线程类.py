#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,func, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)
        self.func = func

    def run(self):
        self.func()


def task():
    time.sleep(1)
    print(11)

obj = MyThread(func=task)
obj.start()

