#!/usr/bin/env python
# -*-coding:utf8-*-
__author__ = "willian"
import time


def tail(file_path):
    with open(file_path, encoding='utf8') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                time.sleep(0.2)


# t = tail('/Users/willian/PycharmProjects/growup/s16/review/a.txt')  # generator
# for line in t:     # 源源不断取数据，相当于next(t)
#     print(line)


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


g = grep('python', tail('a.txt'))

for i in g:
    print(i)
