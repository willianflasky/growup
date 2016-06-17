#!/usr/bin/env python3
import random
"""
print(random.random())
print(random.randint(1,100))
print(random.randrange(1000,2000))
"""
check_code=""
for i in range(4):
    current = random.randint(0,4)
    if current != i:
        tmp = str(chr(random.randint(65,90)))
    else:
        tmp= random.randint(0,9)
    check_code +=str(tmp)
print(check_code)


for i in range(6):
    tm = random.randint(0,4)
    print(tm)