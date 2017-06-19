#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


from multiprocessing import Pool
import time

def f1(arg):
    time.sleep(1)
    print(arg)



if __name__ == '__main__':
    pool=Pool(10)
    for i in range(30):
        #pool.apply(func=f1,args=(i,))
        pool.apply_async(func=f1,args=(i,))

    pool.close() #等任务执行完毕再关闭
    #time.sleep(1)
    #pool.terminate() #当前任务是否执行,立即关闭
    pool.join()


#IO密集型用多线程
#计算密集型用多进程
