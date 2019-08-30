#!/usr/bin/env python
# -*-coding:utf8-*-
__author__ = "willian"



def consumer():
    r = ''
    while True:
        n = yield r     # 第2步. n=1 ；停止   # 第6步. 返回 r="200 OK"；  备注： "n"是收到生产者的数据(赋值给"n"),"r"是返回给生产者的数据.
        if not n:
            return
        print('[消费者] Consuming %s...' % n)  # 第4步.打印
        r = '200 OK'  # 第5步. 赋值

def produce(c):
    c.send(None)       # 第1步. 唤醒consumer进入到yield
    n = 0
    while n < 5:
        n = n + 1
        print('[生产者] Producing %s...' % n)
        r = c.send(n)  # 第3步. 发送数据"1"给comsumer中的yield  # 第7步.收到r="200 OK"
        print('[生产者] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

# yield有2个作用
# 1. 冻结
# 2. 返回数据
