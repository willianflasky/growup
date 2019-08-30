#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


# generator 边执行边计算叫生成器,惰性运算.
# a = (i*i if i > 5 else i for i in range(10))
# print(next(a))
# print(a.__next__())
#


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n += 1
    return "Done"


f = fib(15)
# print(f.__next__())

for i in f:
    print(i)

