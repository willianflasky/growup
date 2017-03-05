#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import random
import string

# print(random.randint(1, 10))
# print(random.randrange(1, 20, 2))
# print(random.sample(range(100), 5))


def check_code(num):
    source = string.digits + string.ascii_letters
    print("".join(random.sample(source, num)))

check_code(6)

