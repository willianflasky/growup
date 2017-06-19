#!/usr/bin/env python3


data=[[col for col in range(4)] for row in range(4)]

#原始展现形式
for i in data:
    print(i)

#旋转90度，方法一
print('---------------------')

for r_index,row in enumerate(data):
    for c_index in range(r_index,len(row)):
        tmp=data[c_index][r_index]
        data[c_index][r_index]=row[c_index]
        data[r_index][c_index]=tmp
    print("*"*10)
    for r in data:print(r)