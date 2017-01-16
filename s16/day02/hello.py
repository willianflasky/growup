#!/usr/bin/env python
# coding:utf8
# Author: willianflasky

# %s %d %f %r

print("My name is %r" % "tom\ntom")


a = 22
b = 56
    #128 64 32 16 8 4 2 1
#a    0  0   0  1 0 1 1 0
#b    0  0   1  1 1 0 0 0

#a&b  0  0   0  1 0 0 0 0  result:16
#a|b  0  0   1  1 1 1 1 0  result:62
#a^b  0  0   1  0 1 1 1 0  result:46


import getpass
