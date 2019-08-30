#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

data = range(1, 4300000000)


def binary_search(find_str, data, count):
    count += 1
    print(count)
    mid = int(len(data)/2)
    if mid == 0:    # data只有一个值的时候.
        if data[mid] == find_str:
            print("find it", find_str)
        else:
            print("not found!")
        return      # 退出,不然报错.

    if data[mid] == find_str:
        print("find it", find_str)

    else:
        if data[mid] > find_str:
            print("must be in left", find_str)
            binary_search(find_str,  data[0:mid], count)
        elif data[mid] < find_str:
            print("must be in right", find_str)
            binary_search(find_str, data[mid+1:], count)
binary_search(100, data, 0)
