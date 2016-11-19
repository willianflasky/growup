#!/usr/bin/env python
#coding:utf8
#Author: willianflasky



from multiprocessing import Process,Array
from multiprocessing import queues
import multiprocessing

def foo(i,arg):
    arg[i] = i +100
    for item in arg:
        print(item)
    print('------------>')

if __name__ == '__main__':
    li=Array('i',10)

    for i in range(10):
        p=Process(target=foo,args=(i,li,))
        #p.daemon=True
        p.start()
        #p.join()  #进程间排队执行
