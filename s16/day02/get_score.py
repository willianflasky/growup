#!/usr/bin/env python
# coding:utf8
# Author:willian

score = int(input("score:"))

if score <= 100 >= 0:
    if score >= 90:
        print("A")

    elif score >= 80:
        print("B")

    elif score >= 70:
        print("B-")

    elif score >= 60:
        print("C")

    else:
        print("D")
else:
    print("不合法!")