#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


import threading
import time
def f1(arg):
    time.sleep(2)
    print(arg)

"""
if __name__ == '__main__':
    for i in range(10):
        t=threading.Thread(target=f1,args=(i,))
        t.start()  #等待被调度
        #t.run     #CPU调用run方法
    """

#第二种方法,自定义类
class MyThread(threading.Thread):
    def __init__(self,func,args):
        self.func=func
        self.args=args
        super(MyThread,self).__init__()

    def run(self):
        self.func(self.args)

if __name__ == '__main__':
    for i in range(10):
        t=MyThread(f1,i)
        t.start()








