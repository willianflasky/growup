#!/usr/bin/env python3

"""
def cash_momey(amount):
    while amount > 0:
        amount -=100
        yield 100
        print("com agent tom")

atm=cash_momey(500)
print(atm.__next__())
print(atm.__next__())


def count(n):
    while n > 0:
        yield n
        n -=1

c=count(10)
print(c)
print(c.__next__())
print(c.__next__())

"""
#生产消费模型,yield即返回值,也可接收值,在这下是接收值.

import time

def consumer(name):
    print("%s 我要准备吃包子"%name)

    while True:
        baozi=yield
        print("包子[%s]来了,被[%s] 吃子!"%(baozi,name))

def producer():
    c1=consumer('tom')
    c2=consumer('tony')
    c1.__next__()
    c2.__next__()
    print("老子开始准备做包子了!")
    for i in range(1,10):
        time.sleep(1)
        print("做了2个包子!")
        c1.send(i)
        c2.send(i)

producer()

