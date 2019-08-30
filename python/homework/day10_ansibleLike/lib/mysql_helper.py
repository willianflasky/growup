#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import pymysql


class MySQLHandler(object):
    def __init__(self, host, port, user, passwd, db, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)     # 返回字典,默认返回元组.

    def select(self, sql, *args):
        self.cursor.execute(sql.format(args[0]))
        result = self.cursor.fetchall()
        return result

    def insert(self, sql, *args):
        self.cursor.execute(sql, args)
        self.commit()

    def update(self, sql, *args):
        self.cursor.execute(sql, args)
        self.commit()

    def delete(self, sql, *args):
        self.cursor.execute(sql, args)
        self.commit()

    def commit(self):
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()


