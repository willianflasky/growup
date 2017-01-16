#!/usr/bin/env python
# coding:utf8
__author__ = "willian"


names = {
    "stu1101": {"name": 'alex', 'age': 22, 'hobbie': 'girl'},
    "stu1102": "jack",
    "stu1103": "rain",
}
"""
# search
print(names["stu1101"]['hobbie'])
print(names.get('stu1108', 'nobody'))

# add
names['stu1104'] = ['yy', 32, 'DBA']

# update
names['stu1104'][0] = "杨板"
print(names["stu1104"][0])

# del
names.pop('stu1104', 'nobody')
del names['stu1103']
print(names)
"""

# 效率高
for key in names:
    print(key, names[key])

# 效率低
for k, v in names.items():
    print(k, v)

# l = [1,2,3]
# print(names.fromkeys(l,[11,22,33]))
# 共享内存

# copy and copy.deepcopy()


