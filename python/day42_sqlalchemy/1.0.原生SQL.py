#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/22 上午8:18
__author__ = "willian"

import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine

engine = create_engine(
    "mysql+pymysql://s6:s6@127.0.0.1:3306/s6?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)


def task(arg):
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select * from users"
    )
    result = cursor.fetchall()
    print(arg)
    time.sleep(3)
    cursor.close()
    conn.close()


for i in range(20):
    t = threading.Thread(target=task, args=(i,))
    t.start()
