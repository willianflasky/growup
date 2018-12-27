#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/23 上午11:45
__author__ = "willian"

import time
import threading
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine("mysql+pymysql://s6:s6@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

# 方式一: 由于无法提供线程共享功能，所以在开发时要注意，在每个线程中自己创建session.
#       自己具有操作数据库的 close commit execute...方法
# session = Session()
# session.close()

# 方式二: scoped_session  支持线程安全，为每个线程创建一个session
#       - threading.Local
#       - 唯一标识

# 源码剖析 第一步：command+单击
session = scoped_session(Session)
session.remove()

"""
session = scoped_session(Session)
session中两个值
    1. self.session_factory
    2. self.registry 中又有两个值, 加括号创建session
        1> self.registry.self.session_factory（createfunc）
        2> self.registry.self.registry（没有写错）
        
"""