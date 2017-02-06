#!/usr/bin/env python
# -*-coding:utf8-*-
import sys
import os
import re

from prettytable import PrettyTable

__author__ = "willian"

class Base(object):
    """
    this base class.
    """

    def __init__(self):
        pass

    def getdata(self, n):
        f = open(n, 'r')
        data1 = f.readlines()
        f.close()
        data = []
        for x in data1:
            data.append(x.strip())
        return data

    def display(self, title, data):
        x = PrettyTable(title)
        x.align["stuff_id"] = "1"  # 以city name 左对齐
        x.padding_width = 1        # 填充宽度
        for i in data:
            temp = i.split(',')
            x.add_row(temp)
        print(x)

class opration():
    """
    for add delete update and select class.
    """

    def __init__(self, title, data, file):
        self.title = title
        self.data = data
        self.map1 = {'stuff_id': 0, 'name': 1, 'age': 2, 'phone': 3, 'dept': 4, 'company': 5, 'enroll_date': 6}
        self.file = file

    def base_like(self, symbol, value, num, column_num=[]):
        count = 0
        r = re.compile(value)
        for row in self.data:
            row_list = row.split(',')
            result = r.findall(row_list[num])
            if result:
                count += 1
                tmp = []
                for i in column_num:
                    tmp.append(row_list[i])
                    print(tmp)
        print("count:", count)

    def select(self, select, column, FROM, table, where, c1, symbol, d1):
        num = self.map1.get(c1)

        if column != '*':
            column_list = column.split(',')
            column_num = []
            # column change to number!
            for x in column_list:
                column_num.append(self.map1.get(x))

            if symbol == 'like':
                self.base_like('like', d1, num, column_num)

            elif symbol == '=':
                count = 0
                for row in self.data:
                    row_list = row.split(',')
                    if row_list[num] == d1:
                        count += 1
                        tmp = []
                        for i in column_num:
                            tmp.append(row_list[i])
                        print(tmp)
                print("count:", count)
            else:
                count = 0
                for row in self.data:
                    row_list = row.split(',')
                    result = row_list[num] + symbol + d1
                    if eval(result):
                        count += 1
                        tmp = []
                        for i in column_num:
                            tmp.append(row_list[i])
                        print(tmp)
                print("count:", count)

        elif column == '*':
            if symbol == 'like':
                count = 0
                r = re.compile(d1)
                for row in self.data:
                    row_list = row.split(',')
                    result = r.findall(row_list[num])
                    if result:
                        count += 1
                        print(row)
                print("count:", count)

            elif symbol == '=':
                count = 0
                for row in self.data:
                    row_list = row.split(',')
                    if row_list[num] == d1:
                        count += 1
                        print(row)
                print("count:", count)

            else:
                count = 0
                for row in self.data:
                    row_list = row.split(',')
                    result = row_list[num] + symbol + d1
                    if eval(result):
                        count += 1
                        print(row)
                print("count:", count)

    def add(self, x_list):
        write_list = []
        f1 = open(self.file, 'r+')
        all_data = f1.readlines()
        stuff_id = all_data[-1].split(',')[0]
        f1.close()

        for line in all_data[1:]:
            tmp = line.split(",")
            if x_list[2] in tmp[3]:
                print("主键:phone冲突!")
                raise Exception

        write_list.append(str(int(stuff_id) + 1))
        for i in x_list:
            write_list.append(i)
        f2 = open(self.file, 'a+')
        write_str = ",".join(write_list)
        write_str = write_str + "\n"
        f2.writelines(write_str)
        f2.close()

    def delete(self, number):
        f3 = open(self.file, 'r+')
        data = f3.readlines()
        title = data[0]
        from collections import OrderedDict
        tmp_dict = OrderedDict()

        for i in data[1:]:
            tmp_list = i.split(',', 1)
            tmp_dict[tmp_list[0]] = tmp_list[1]

        if number in tmp_dict:
            tmp_dict.pop(number)
        else:
            print("没有这条数据!")

        write_back = []
        write_back.append(title)
        for i in tmp_dict:
            write_back.append(i+','+tmp_dict[i])
        f3.close()

        with open(self.file, 'w') as f4:
            for x in write_back:
                f4.writelines(x)

    def update(self, column, condition, value):
        data_list = []
        column_list = column.split('=')
        condition_num = self.map1.get(condition)
        set_num = self.map1.get(column_list[0])
        for x in self.data:
            x_list = x.split(',')
            data_list.append(x_list)

        for lst in data_list:
            if lst[condition_num] == value:
                lst[set_num] = column_list[1]

        # write back; list change to  string
        writeback_list = []
        writeback_list.append(self.title + "\n")

        for lst in data_list:
            tmp = ",".join(lst)
            tmp = tmp + "\n"
            writeback_list.append(tmp)

        with open(self.file, 'w') as f5:
            for x in writeback_list:
                f5.writelines(x)

if __name__ == '__main__':
    pass

