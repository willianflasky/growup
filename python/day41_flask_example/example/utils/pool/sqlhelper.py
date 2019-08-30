#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/20 下午8:44
__author__ = "willian"

from utils.pool import db_pool


class SQLHelper(object):
    def __init__(self):
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = db_pool.SingletonDBPool()
        self.conn = self.conn.connect()
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def fetchone(self, sql, params):
        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        return result

    def fetchall(self, sql, params):
        self.cursor.execute(sql, params)
        result = self.cursor.fetchall()
        return result

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
