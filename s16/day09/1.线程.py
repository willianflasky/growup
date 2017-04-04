#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import threading
import time


def task(arg):
    time.sleep(1)
    print(arg)


for i in range(5):
    t = threading.Thread(target=task, args=[i, ])  # 主线程创建一个线程.
    t.setDaemon(True)   # 主线程终止,不等待子线程.default False. (只能设置在start上面.)
    t.start()           # 等待CPU调度
    # t.jon()           # 一直等. 串行执行
    t.join(1)           # 只等1秒 串行执行了

print('end')
