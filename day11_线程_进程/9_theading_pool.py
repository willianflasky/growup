#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
import queue
import threading,time

class ThreadPool(object):
    def __init__(self,maxsize=5):
        self.maxsize=maxsize
        self._q= queue.Queue(maxsize)
        for i in range(maxsize):
            self._q.put(threading.Thread)

    def get_thread(self):
        return self._q.get()

    def add_thread(self):
        self._q.put(threading.Thread)


pool = ThreadPool(50)

def task(arg,p):
    print(arg)
    time.sleep(2)
    p.add_thread()


for i in range(100):
    cls=pool.get_thread()
    t=cls(target=task,args=(i,pool,))
    t.start()

