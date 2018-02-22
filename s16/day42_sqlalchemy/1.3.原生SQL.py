#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/22 下午12:40
__author__ = "willian"

import time
import threading

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.engine.result import ResultProxy
from models import UserInfo, Hosts

engine = create_engine("mysql+pymysql://s6:s6@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

session = Session()

# 查询
# cursor = session.execute('select * from users')
# result = cursor.fetchall()

# 添加
cursor = session.execute('insert into UserInfo(name) values(:value)', params={"value": 'wupeiqi'})
session.commit()
# cursor = session.execute('update UserInfo set name=:value where id=1', params={'value': "alex099"})
# session.commit()
print(cursor.lastrowid)
