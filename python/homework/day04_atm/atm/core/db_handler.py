#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from atm.conf import settings
import os
import json


def file_db_handle(conn_params):
    """
    转发功能
    :param conn_params:
    :return:
    """
    return file_execute


def file_execute(sql, **kwargs):
    """
    返回json的用户数据.
    :param sql:
    :param kwargs:
    :return:
    """
    conn_params = settings.DATABASE
    db_path = '%s/%s' % (conn_params['path'], conn_params['name'])

    sql_list = sql.split("where")
    if sql_list[0].startswith("select") and len(sql_list) > 1:
        column, val = sql_list[1].strip().split("=")

        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            if os.path.isfile(account_file):
                with open(account_file, 'r') as f:
                    account_data = json.load(f)
                    return account_data
            else:
                exit("\033[31;1mAccount [%s] does not exist!\033[0m" % val)

    elif sql_list[0].startswith("update") and len(sql_list) > 1:
        column, val = sql_list[1].strip().split("=")
        if column == 'account':
            account_file = "%s/%s.json" % (db_path, val)
            if os.path.isfile(account_file):
                account_data = kwargs.get("account_data")
                with open(account_file, 'w') as f:
                    acc_data = json.dump(account_data, f)
                return True


def db_handler():
    """
    判断数据库类型.
    :return:
    """
    conn_params = settings.DATABASE
    if conn_params['engine'] == 'file_storage':
        return file_db_handle(conn_params)
    elif conn_params['engine'] == 'mysql':
        pass

