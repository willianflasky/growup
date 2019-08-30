#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


def read_file(fpath):
    with open(fpath, 'rb') as f:
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                return False


f = read_file('access.log')

# for line in f:
#     print(line.decode('utf8'), end="")

tmp = b''
for line in f:
    tmp += line

print(tmp.decode('utf8'))
