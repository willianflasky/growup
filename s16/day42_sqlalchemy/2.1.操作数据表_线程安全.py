#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/22 上午8:55
__author__ = "willian"

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from models import UserInfo

engine = create_engine("mysql+pymysql://s6:s6@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

"""
# 线程安全，基于本地线程实现每个线程用同一个session
# 特殊的：scoped_session中有原来方法的Session中的一下方法：

public_methods = (
    '__contains__', '__iter__', 'add', 'add_all', 'begin', 'begin_nested',
    'close', 'commit', 'connection', 'delete', 'execute', 'expire',
    'expire_all', 'expunge', 'expunge_all', 'flush', 'get_bind',
    'is_modified', 'bulk_save_objects', 'bulk_insert_mappings',
    'bulk_update_mappings',
    'merge', 'query', 'refresh', 'rollback',
    'scalar'
)
"""
session = scoped_session(Session)

# ############# 执行ORM操作 #############
obj4 = UserInfo(name="alex4")
session.add(obj4)

# 提交事务
session.commit()
# 关闭session
session.close()
