#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

data = [1, 2, 3, 7, 8, 9]

def binary_search(find_string, data_list):
    mid = int(len(data_list)/2)
    if mid == 0:
        if data_list[mid] == find_string:
            print("find it!")
        else:
            print("not value!")
        return

    if data_list[mid] == find_string:
        print('find it', find_string)
    elif data_list[mid] > find_string:
        print("in left", data_list[:mid])
        binary_search(find_string, data_list[:mid])
    elif data_list[mid] < find_string:
        print("in right", data_list[mid:])
        binary_search(find_string, data_list[mid:])

binary_search(2, data)
