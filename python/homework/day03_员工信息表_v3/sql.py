#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

"""
    1.sql = input("sql> ").strip()
    2.sql_dic = sql解析(sql)
    3.res = sql执行(sql_dic)
    4.格式化输出res

"""


# 第一部分SQL解析
def sql_parse(sql):     # insert delete update select
    """
    把SQL字符串切分,提取命令信息,然后分发给具体的函数去解析.
    :param sql:
    :return:
    """
    parse_func = {
        'insert': insert_parse,
        'update': update_parse,
        'delete': delete_parse,
        'select': select_parse,
    }

    sql_l = sql.split(" ")
    func = sql_l[0]
    res = ""
    if func in parse_func:
        res = parse_func[func](sql_l)

    return res


def insert_parse(sql_l):
    """
    定义INSERT语句的语法结构,执行解析操作,返回sql_dic
    :param sql:
    :return:
    """


def delete_parse(sql_l):
    """
        定义DELETE语句的语法结构,执行解析操作,返回sql_dic
    :param sql:
    :return:
    """
    pass


def update_parse(sql_l):
    """
        定义UPDATE语句的语法结构,执行解析操作,返回sql_dic

    :param sql:
    :return:
    """
    pass


def select_parse(sql_l):
    """
        定义SELECT语句的语法结构,执行解析操作,返回sql_dic
    :param sql:
    :return:
    """
    sql_dic = {
        'func': select,
        'select': [],   # 字段
        'from': [],     # 数据, 表
        'where': [],    # filter
        'limit': [],    # limit
    }

    return handle_parse(sql_l, sql_dic)

def handle_parse(sql_l, sql_dic):
    """
    执行SQL解析操作,返回sql_dic
    :param sql:
    :return:
    """
    pass


# 第二部分SQL执行
def sql_action(sql_dic):
    """
    从字典sql_dic当中提取命令,分发给集体的命令执行函数执行.
    :param sql_dic:
    :return:
    """
    pass


def insert(sql_dic):
    pass


def delete(sql_dic):
    pass


def update(sql_dic):
    pass


def select(sql_dic):
    pass


if __name__ == '__main__':
    while True:
        sql = input("sql> ").strip()
        if sql == 'exit':
            break
        if len(sql) == 0:
            continue

        sql_dic = sql_parse(sql)

        if len(sql_dic) == 0:
            continue
        res = sql_action(sql_dic)
