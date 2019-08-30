#!/usr/bin/env python
# coding:utf8
# Author:willian

for i in range(10):
    if i == 5:
        for j in range(10):
            print("inner loop:", j)
            if j == 6:
                break
        continue
    print("loop", i)
