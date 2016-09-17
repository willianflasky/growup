#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import queue
import threading
import time

q=queue.Queue(20)

def productor(arg):
    """
    买票
    :param arg:
    :return:
    """
    q.put(str(arg)+'-包子')

def consumer(arg):
    while True:
        print(arg,q.get())
        time.sleep(2)


for i in range(3):
    t=threading.Thread(target=productor,args=(i,))
    t.start()

for j in range(20):
    t=threading.Thread(target=consumer,args=(j,))
    t.start()

