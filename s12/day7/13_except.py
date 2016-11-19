#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
"""
while True:
    num1=input('num1:')
    num2=input('num2:')
    try:
        num1=int(num1)
        num2=int(num2)
        ret=num1+num2
    except Exception as e:
        print(e)
"""
"""
try:
    raise ValueError("主动错误")
    i='tom'
    int(i)
    print(123)
except ValueError as ex:
    print('=>>',ex)
except Exception as ex:
    print("-->",ex)
else:
    pass

finally:
    print('finally!')

"""
"""
assert 1==2 #报错
assert 1==1 #不报错
"""


#自定义异常
class myException(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

try:
    raise myException('我主动报错')
except myException as e:
    print(e)