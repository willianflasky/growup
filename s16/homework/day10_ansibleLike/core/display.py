#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from lib import mysql_helper
from conf.settings import *


def display(user_dic):
    conn = mysql_helper.MySQLHandler(db_host, db_port, db_user, db_pass, db_name)
    # result = conn.select('select * from hosts where id in (select hosts_id from users2hosts where users_id = {0})', user_dic['id'])
    result = conn.select('select h.ip,h.port,h.username,h.password from hosts as h right join users2hosts as uh on h.id = uh.hosts_id where uh.users_id = {0}', user_dic['id'])

    if len(result) != 0:
        print("\033[33;1m\n管理主机地址:\033[0m")
        for host in result:
            print("\033[33;1m\t{0}\033[0m".format(host['ip']))
        return True, result
    else:
        return False



