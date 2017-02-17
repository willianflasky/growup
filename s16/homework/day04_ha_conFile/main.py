#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import os
import sys
import re

conf_file = "main.conf"
base_dir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))


def open_file(mode='r'):
    with open("{0}/{1}".format(base_dir, conf_file), mode) as f:
        if mode == 'r':
            data = f.readlines()
            return data
        else:
            pass


def read():
    data = open_file()
    for line in data:
        print(line, end="")


def write(arg):
    pass


def main_read():
    flag = False
    while True:
        inp = input(">:").strip()
        if len(inp) == 0:
            continue
        elif re.search("(.*)\.(.*)\.(.*)", inp):
            match_string = ".".join(re.search("(.*)\.(.*)\.(.*)", inp).groups())
            data = open_file()
            tmp_list = []
            for line in data:
                if flag:
                    if line.strip().startswith("server"):
                        tmp_list.append(line)
                    else:
                        flag = False
                elif re.search("^backend( +)%s" % match_string, line):
                    flag = True
            for x in tmp_list:
                print(x.strip())

        else:
            print("你查找的配置块不在.")


if __name__ == '__main__':
    choice = input(">>:").strip()
    main_read()






