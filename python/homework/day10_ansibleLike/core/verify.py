#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import getpass

from lib import mysql_helper
from conf.settings import *


def verify():
    conn = mysql_helper.MySQLHandler(db_host, db_port, db_user, db_pass, db_name)
    result = conn.select('select * from {0}', 'users')

    count = 3
    while count > 0:
        _username = input("请输入用户名:").strip()
        _password = getpass.getpass("请输入密码:").strip()  # pycharm调试不好用

        for user_dic in result:
            if _username == user_dic['username'] and _password == user_dic['password']:
                print("\033[32;1m验证成功!\033[0m")
                return True, user_dic
        count -= 1

    else:
        print("\033[31;1m超过3次!\033[0m")
        return False

