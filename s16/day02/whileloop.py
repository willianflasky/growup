#!/usr/bin/env python
# coding:utf8
# __author__ = "willian"

import time

start1 = time.time()
count = 0
while True:
    if count == 10000000:
        break
    count += 1
print("start1:", time.time() - start1)

count = 0
start2 = time.time()
while count < 10000000:
    count += 1
print("start2", time.time() - start2)