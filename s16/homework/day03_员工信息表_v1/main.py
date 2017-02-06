#!/usr/bin/env python
# -*-coding:utf8-*-
import os
import sys
from tools import Base
from tools import opration

__author__ = "willian"

curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curr_dir)

info = "{0}/info.txt".format(curr_dir)

p1 = Base()
data = p1.getdata(info)
title = data[0].split(',')
p1.display(title, data[1:])

p2 = opration(data[0], data[1:], info)

while True:
    choice = input("\033[33;1mmysql>\033[0m")
    if len(choice) == 0:
        continue

    if choice.startswith('select') or choice.startswith('SELECT'):
        sql = choice.split(' ')
        try:
            p2.select(select=sql[0], column=sql[1], FROM=sql[2], table=sql[3], where=sql[4], c1=sql[5], symbol=sql[6], d1=sql[-1])
        except Exception as e:
            print("异常!")
            print(e)
            continue

    elif choice.startswith('insert') or choice.startswith("INSERT"):
        try:
            ret = choice.split(' ')[1:]
            p2.add(ret)
        except Exception as e:
            print("异常!")
            print(e)
            continue
    elif choice.startswith('delete') or choice.startswith("DELETE"):
        try:
            sql_list = choice.split(' ')[-1]
            p2.delete(sql_list)
        except Exception as e:
            print(e)
            continue

    elif choice.startswith('update') or choice.startswith('UPDATE'):
        try:
            sql_list = choice.split(' ')
            p2.update(sql_list[3], sql_list[5], sql_list[7])
        except Exception as e:
            print("Update 异常!")
            print(e)
            continue
    else:
        continue

