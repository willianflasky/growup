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
            return None


def read():
    data = open_file()
    for line in data:
        print(line, end="")


def write(arg):
    arg = eval(arg)         # str change to dict type
    src_data = open_file()
    if isinstance(arg, dict):
        if 'backend' in arg and 'record' in arg:
            record_url = arg.get('backend')
            record_value_dic = arg.get("record")
            s, w, m = record_value_dic.get('server'), record_value_dic.get('weight'), record_value_dic.get('maxconn')
            res = "\tserver {0} {0} weight {1} maxconn {2}\n".format(s, w, m)

        with open('{0}/{1}.bak'.format(base_dir, conf_file), 'w') as f1:
            for line in src_data:
                f1.write(line)
                if re.search("^backend( +){0}".format(record_url), line):
                    f1.write(res)
        os.renames("{0}/{1}.bak".format(base_dir, conf_file), "{0}/{1}".format(base_dir, conf_file))

    else:
        print("unknown input!")


def main_read():
    flag = False
    while True:
        inp = input("read>:").strip()
        if len(inp) == 0:
            continue
        elif inp == 'q':
            break
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
    while True:
        print("1.查看\n2.修改\n3.退出")
        choice = input("=>").strip()
        if len(choice) == 0:
            continue
        elif choice.isdigit():
            choice = int(choice)
            if choice == 1:
                main_read()
            elif choice == 2:
                while True:
                    inp = input("write>").strip()
                    if len(inp) == 0:
                        continue
                    elif inp == 'q':
                        break
                    else:
                        write(inp)
            elif choice == 3:
                exit()
            else:
                print("unknown number!")
                continue
        else:
            print("unknown symbol!")
            continue








