#!/usr/bin/env python
"""
f=open('test.log','w')
f.write('this line 1\n')
f.write('this line 2\n')
f.write('this line 3\n')

f=open('test.log','r')
print(f.read())
f.close()

f=open('test.log','a')
f.write("6\n")
f.write("7\n")
f.close()

"""

f=open('test.log','w+')
f.write('new line\n')
print("data:",f.read())