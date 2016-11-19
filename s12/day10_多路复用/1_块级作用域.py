#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

#python无块级作用域
"""
if 1 == 1:
    name='aelx'

print(name)
#python作用域在函数中


def func():
    name='tom'

func()

print(name)
"""
"""
name='alex1'
def f1():
    name='eric'
    print(name)

f1()
"""
#作用域链,本级找不到去上级找.


#python的作用域在执行之前已经固定,在那里执行不重要.
"""
name='tom'
def f1():
    print(name)

def f2():
    name='eric'
    f1()

f2()



name='tom'
def f1():
    print(name)

def f2():
    name='eric'
    return f1

ret=f2()
ret()
"""

"""
li=[lambda :x for x in range(10)]

li=[]
def i in range(10):
    def f1():
        return i

    li.append(f1)

li[0]()

"""

li=[]
for i in range(10):
    def f1(x=i):
        return x
    li.append(f1)

print(li[3]())
