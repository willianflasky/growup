#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

a = {1, 3, 5, 7, 10}
b = {2, 3, 4, 5, 6, 8}

# 交集
print(a & b)
print(a.intersection(b))
print(a.intersection_update(b))  # a = a.intersection(b)
# print(a, b)

# 差集
print(b - a)
print(a - b)
print(b.difference(a))

# 并集
print(a | b)

# 对称差集
print(a ^ b)

