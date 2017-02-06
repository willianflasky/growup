#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


def calc(n):
    print(n)
    if int(n/2) > 0:
        n = calc(int(n/2))
    return n

calc(10)

print("result:", calc(10))