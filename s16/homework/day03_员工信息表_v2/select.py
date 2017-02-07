#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


import re


def select_process(arg):
    print(arg)


def select(arg):
    tmp = None
    if re.search("select +(.*) +from +(.*) +where +(.*)", arg):
        tmp = re.search("select +(.*) +from +(.*) +where +(.*)", arg).groups()
    elif re.search("select +(.*) +from +(.*)", arg):
        tmp = re.search("select +(.*) +from +(.*)", arg).groups()
    else:
        print("格式错误!")

    return tmp

if __name__ == '__main__':
    ret = select("select * from t1 where name = t")
    print(ret)
