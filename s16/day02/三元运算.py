#!/usr/bin/env python
# coding:utf8
__author__ = "willian"

# 三元运算
a = 2
b = 3
c = a + b if a > b else a - b
print(c)


# find rain
names = [1, 2, 3, 4, 'rain', 5, 6, 'rain']
first_index = names.index('rain')
second_index = names[first_index + 1:].index('rain')
del names[first_index + second_index + 1]
print(names)

# extend
names += [11, 22, 33]
names.extend([111, 222, ])
print(names)

names.pop(4)
print(names)

name2 = [['alex', 22], ['teacher', 3000], ['oldboy', 56]]

print(name2)
print(name2[0][1])
name2[1][1] = 30000
print(name2[1][1])

#

