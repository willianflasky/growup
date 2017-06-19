#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

from multiprocessing import Process
from multiprocessing import queues
import multiprocessing

def foo(i,arg):
    arg.put(i)
    print('say hi',i,arg.qsize())

if __name__ == '__main__':
    li=queues.Queue(20,ctx=multiprocessing)

    for i in range(10):
        p=Process(target=foo,args=(i,li,))
        #p.daemon=True
        p.start()
        #p.join()  #进程间排队执行
