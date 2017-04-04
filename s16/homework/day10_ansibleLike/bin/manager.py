#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import os
import sys

BASE_DIR = os.path.normpath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.insert(0, BASE_DIR)

from lib import mysql_helper
from lib import manage_helper


menu = {
    1: [manage_helper.Manage.select_user, '查询用户'],
    2: [manage_helper.Manage.select_host, '查询主机'],
    3: [manage_helper.Manage.select_user_host, '查询用户的主机'],
    4: [manage_helper.Manage.insert_user, '增加用户'],
    5: [manage_helper.Manage.insert_host, '增加主机'],
    6: [manage_helper.Manage.insert_user_host, '增加用户的主机'],
    7: [manage_helper.Manage.update_user, '修改用户密码'],
    8: [manage_helper.Manage.update_host, '修改主机'],
    # 9: [manage_helper.Manage.delete_user, '删除用户'],
    # 11: [manage_helper.Manage.delete_host, '删除主机'],
    # 12: [manage_helper.Manage.delete_user_host, '删除用户的主机']
}


def main():
    while True:
        for i, k in enumerate(menu, 1):
            print(i, menu[k][1])

        inp = input(">>>").strip()
        if len(inp) == 0:
            continue
        if inp == 'exit':
            break
        if inp.isdigit():
            try:
                menu[int(inp)][0]()
            except KeyError as e:
                print("\033[31;1mnot found number!\033[0m".center(60, '-'))
        else:
            print("\033[31;1mnot found characters!\033[0m".center(60, '-'))

if __name__ == '__main__':
    main()
