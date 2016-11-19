#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
import threading,time

def f1(arg):
    time.sleep(5)
    print(arg)



t=threading.Thread(target=f1,args=(123,))
#t.setDaemon(True) #表示主线程不等子线程.
t.start()
t.join(2)    #表示主线程,等待..直到子线程执行完毕. 参数表示主线程在些最多等几秒.
print('end')