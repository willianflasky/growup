#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


from multiprocessing import Process,Manager
from multiprocessing import queues
import multiprocessing

def foo(i,arg):
    arg[i] = i + 100
    print(arg.values())

if __name__ == '__main__':
    obj=Manager()
    li=obj.dict()

    for i in range(10):
        p=Process(target=foo,args=(i,li,))
        #p.daemon=True
        p.start()
        #p.join()  #进程间排队执行
    import time
    time.sleep(3)
