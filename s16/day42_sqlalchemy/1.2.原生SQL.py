#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/22 上午8:34
__author__ = "willian"

import time
import threading
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.result import ResultProxy

engine = create_engine("mysql+pymysql://s6:s6@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)


def task(arg):
    cur = engine.execute("select * from users")
    result = cur.fetchall()
    cur.close()
    print(arg)


for i in range(20):
    t = threading.Thread(target=task, args=(i,))
    t.start()
