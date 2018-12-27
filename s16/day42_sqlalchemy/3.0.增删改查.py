#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/22 上午9:01
__author__ = "willian"

import time
import threading
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from models import Choice

engine = create_engine("mysql+pymysql://s6:s6@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

session = Session()

# ################ 添加 ################
"""
# 方法一
obj1 = UserInfo(name="wupeiqi")
session.add(obj1)

# 方法二：批量添加
session.add_all([
    UserInfo(name="willian1"),
    UserInfo(name="willian2"),
    Hosts(name="c1.com", ctime=datetime.datetime.now()),
])
session.commit()
"""
# session.add(Choice(name="alex", types=1))
# session.commit()

# ret = session.query(Choice).all()
# for i in ret:
#     print(i.types.code, i.types.value)

# ################ 删除 ################
"""
session.query(UserInfo).filter(UserInfo.id >= 8).delete()
session.commit()
"""

# ################ 修改 ################
"""
session.query(UserInfo).filter(UserInfo.id >= 2).update({"name": "099"})
session.query(UserInfo).filter(UserInfo.id > 0).update({UserInfo.name: UserInfo.name + "099"}, synchronize_session=False)   # string相加
session.query(UserInfo).filter(UserInfo.id == 14).update({"id": UserInfo.id + 10},
                                                       synchronize_session="evaluate")  # number相加
session.commit()
"""

# ################ 查询 ################
"""
r1 = session.query(UserInfo).all()
r2 = session.query(UserInfo.name.label('xx'), UserInfo.id).all()
r3 = session.query(UserInfo).filter(UserInfo.name == "alex099").all()
r4 = session.query(UserInfo).filter_by(name='alex099').all()
r5 = session.query(UserInfo).filter_by(name='alex099').first()
r6 = session.query(UserInfo).filter(text("id<:value and name=:name")).params(value=3, name='alex099').order_by(UserInfo.id).all()
r7 = session.query(UserInfo).from_statement(text("SELECT * FROM UserInfo where name=:name")).params(name='alex099').all()
"""



session.close()
