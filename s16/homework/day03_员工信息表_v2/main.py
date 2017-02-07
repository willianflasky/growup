#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

"""
一.需求分析:
    1.select name,age from t1 where age > 22
    2.select * from t1 where dept = dev
    3.select * from t1 where enroll_date like 2013
    4.count:
    5.主键自增
    6.delete [ID]
    7.update t1 set name=tom where dept = dev
二.公用操作:
    1.获取数据
    2.display
    3.读和写.
"""

import os
import sys
import re
from prettytable import PrettyTable


# 变量定义:
curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curr_dir)
file_name = "info.txt"
info_file = "{0}/{1}".format(curr_dir, file_name)


# 定义函数:
def display(title_list, data_list, first_column='stuff_id'):
    """
    使用方法:
        title = ['name', 'age']
        data = ['tom,28', 'eric,30']
        display(title, data)
    :param first_column:
    :param title_list:
    :param data_list:
    :return:
    """
    x = PrettyTable(title_list)
    x.align[first_column] = "1"  # 以city name 左对齐
    x.padding_width = 1          # 填充宽度
    for i in data_list:
        temp = i.split(',')
        x.add_row(temp)
    print(x)


def getdata(file):
    """
    功能:
        1.打开文件获取数据.
        2.去掉"\n"
    :param file:
    :return:
    """
    f = open(file, 'r')
    data1 = f.readlines()
    f.close()
    data = []
    # 去掉换行"\n"
    for line in data1:
        data.append(line.strip())
    return data


def writeback(title, data, info_file=info_file):
    writeback_list = []
    writeback_list.append(title + "\n")
    for line in data:
        line = line + "\n"
        writeback_list.append(line)
    with open(info_file, 'w') as f:
        for line in writeback_list:
            f.writelines(line)


# 定义主类:
class BASE(object):
    def __init__(self, file, data, title):
        self.file = file
        self.map1 = {'stuff_id': 0, 'name': 1, 'age': 2, 'phone': 3, 'dept': 4, 'company': 5, 'enroll_date': 6}
        self.data = data
        self.title = title

    def check_sql(self, sql):
        tmp_tuple = None
        if re.search("select +(.*) +from +(.*) +where +(.*)", sql):
            tmp_tuple = re.search("select +(.*) +from +(.*) +where +(.*)", sql).groups()

        elif re.search("select +(.*) +from +(.*)", sql):
            tmp_tuple = re.search("select +(.*) +from +(.*)", sql).groups()
        else:
            print("sql syntax error!")
            raise AssertionError
        return tmp_tuple

    def __column_process(self, sql):
        column_list = sql.split(",")
        column_number = []
        for column in column_list:
            column_number.append(self.map1.get(column))

        if None in column_number or len(column_number) == 0:
            print("字段错误!")
            raise AssertionError

        return column_list, column_number

    def __where_process(self, sql):
        if re.search("(.*) +(like|>|<|=) +(.*)", sql[-1]):
            condition_list = sql[-1].split(" ")
            condition_num = self.map1.get(condition_list[0])
            r = re.compile(condition_list[-1].strip())
            for_display = []
            count = 0
            if sql[0] == "*":
                column_number = []
                column_list = []
                ret = self.__where_sub(sql[0], r, condition_num, condition_list, column_number, for_display, count)
                return ret[0], ret[1]
            else:
                result = self.__column_process(sql[0])
                column_list, column_number = result[0], result[1]
                ret = self.__where_sub(sql[0], r, condition_num, condition_list, column_number, for_display, count)
                return column_list, ret[0], ret[1]

        else:
            print("condition error!")
            raise AssertionError

    def __where_sub(self, star, r, condition_num, condition_list, column_number, for_display=[], count=0):
        for line in self.data:
            line_list = line.split(',')
            if condition_list[1] == "like":
                result = r.findall(line_list[condition_num])
            elif condition_list[1] == "=":
                if line_list[condition_num] == condition_list[-1]:
                    result = True
                else:
                    result = False
            else:
                calc = line_list[condition_num] + condition_list[1].strip() + condition_list[2].strip()
                if eval(calc):
                    result = True
                else:
                    result = False

            if result:
                count += 1
                tmp = ""
                if star == "*":
                    for_display.append(line)
                else:
                    for num in column_number:
                        tmp = tmp + "," + line_list[num]
                        tmp = tmp.lstrip(',')
                    for_display.append(tmp)
        return for_display, count

    def not_where(self, sql):
        if sql[0] == "*":
            title = self.title.split(',')
            count = len(self.data)
            display(title, self.data)
            print("count:", count)
        else:
            result = self.__column_process(sql[0])
            column_list, column_number = result[0], result[1]
            for_display = []
            count = 0
            for line in self.data:
                count += 1
                tmp = ""
                line_list = line.split(',')
                for num in column_number:
                    tmp = tmp + "," + line_list[num]
                    tmp = tmp.lstrip(',')
                for_display.append(tmp)
            display(column_list, for_display)

    def with_where(self, sql):
        if sql[0] == "*":
            result = self.__where_process(sql)
            display(self.title.split(','), result[0])
            print("count:", result[-1])
        else:
            result = self.__where_process(sql)
            column_list, for_display, count = result[0], result[1], result[2]
            display(column_list, for_display, column_list[0])
            print("count:", count)

    def insert(self, new_line, data, phone):
        # get_max_id
        id_list = []
        for line in data:
            stuffid = line.split(',')[0]
            id_list.append(stuffid)
        id_list.sort()
        max_id = int(id_list[-1]) + 1

        # phone
        phone_list = []
        for line in data:
            tmp_phone = line.split(',')[3]
            phone_list.append(tmp_phone)

        if phone in phone_list:
            print("主健冲突!")
        else:
            # insert data
            new_insert = str(max_id) + ',' + ",".join(new_line)
            data.append(new_insert)

    def delete(self, index_number, data):
        for line in data:
            if line.startswith(index_number):
                del_line = line

        data.pop(data.index(del_line))

    def update(self, column, data, condition, value):
        column_list = column.split("=")     # 字段和值
        set_number = self.map1.get(column_list[0])
        condition_number = self.map1.get(condition)
        data_list = []

        for line in data:
            line = line.split(',')
            data_list.append(line)

        for lst in data_list:
            if lst[condition_number] == value:
                lst[set_number] = column_list[1]

        data = []
        for one in data_list:
            one = ','.join(one)
            data.append(one)
        return data

# 实例化
data = getdata(info_file)
title = data[0]
data = data[1:]
OBJ = BASE(info_file, data, title)


def main():
    while True:
        choice = input("\033[33;1mmysql>\033[0m")
        if len(choice) == 0:
            continue
        elif choice.startswith('select') or choice.startswith('SELECT'):
            sql_tuple = OBJ.check_sql(choice)
            if len(sql_tuple) == 0:
                continue
            elif len(sql_tuple) == 2:
                try:
                    OBJ.not_where(sql_tuple)
                except AssertionError:
                    continue
            elif len(sql_tuple) == 3:
                try:
                    OBJ.with_where(sql_tuple)
                except AssertionError:
                    continue
            else:
                print("error!")
                continue

        elif choice.startswith('insert') or choice.startswith('INSERT'):
            # 获取数据
            all_data = getdata(info_file)
            title = all_data[0]
            data = all_data[1:]

            # 处理数据
            ret = choice.split(" ")
            if len(ret[1:]) != 6:
                print("insert input error!")
                continue
            else:
                try:
                    OBJ.insert(ret[1:], data, ret[3])
                except Exception as e:
                    print(e)
                    continue
            # 回写数据
            writeback(title, data)

        elif choice.startswith('delete') or choice.startswith('DELETE'):
            # 获取数据
            all_data = getdata(info_file)
            title = all_data[0]
            data = all_data[1:]

            # 处理数据
            ret = choice.split(' ')
            if len(ret) > 2:
                print("input error!")
                continue
            else:
                try:
                    OBJ.delete(ret[-1], data)
                except UnboundLocalError:
                    print("not found!")
                    continue

            # 回写数据
            writeback(title, data)

        elif choice.startswith('update') or choice.startswith('UPDATE'):
            # 获取数据
            all_data = getdata(info_file)
            title = all_data[0]
            data = all_data[1:]

            # 处理数据
            sql = choice.split(' ')
            if len(sql) != 8:
                print("格式错误!")
                continue
            else:
                data = OBJ.update(sql[3], data, sql[5], sql[-1])
                writeback(title, data)

        elif choice == 'showme' or choice == 'SHOWME':
            all_data = getdata(info_file)
            title = all_data[0]
            data = all_data[1:]
            display(title.split(','), data)
        else:
            print("\033[31;1m你的输入我不能理解:\n[{0}]\033[0m".format(choice))
            continue

if __name__ == '__main__':
    main()

