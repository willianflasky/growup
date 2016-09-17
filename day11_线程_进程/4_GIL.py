#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import threading,time

NUM=10

def func(i,l):
    global NUM
    #lock
    l.acquire()
    NUM -= 1
    time.sleep(2)
    print(i,NUM)
    #unlock
    l.release()

#lock=threading.Lock() #不支持多层锁
#lock=threading.RLock()
lock=threading.BoundedSemaphore(5)  #信号量


for i in range(30):
    t=threading.Thread(target=func,args=(i,lock,))
    t.start()

