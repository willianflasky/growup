#!/usr/bin/env python3
"""
#递归算法
def calc(n):
    print(n)
    if n/2 >1:
        res= calc(n/2)
        print('res:',res)
    print('N:',n)
    return n

calc(10)

#斐波那契

def func(arg1,arg2,stop):
    if arg1 ==0:
        print(arg1,arg2)
    arg3=arg1+arg2
    print(arg3)
    if arg3< stop:
        func(arg2,arg3,stop)

func(0,1,30)
"""

#实例 二分查找又称折半查找
def binary_search(data_source,find_n):
    mid=int(len(data_source)/2)
    if len(data_source) >= 1:
        if data_source[mid] > find_n:
            print("data in left of [%s]"%data_source[mid])
            binary_search(data_source[:mid],find_n)
        elif data_source[mid] < find_n:
            print("data in right of [%s]"%data_source[mid])
            binary_search(data_source[mid:],find_n)
        else:
            print("find:[%s]"%data_source[mid])

    else:
        print("cannot find...")


if __name__=="__main__":
    data=list(range(1,11))
    binary_search(data,1)