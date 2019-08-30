#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/22 上午8:43
__author__ = "willian"

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import UserInfo

engine = create_engine("mysql+pymysql://s6:s6@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

# 每次执行数据库操作时，都需要创建一个session
session = Session()

# ############# 执行ORM操作 #############
# obj1 = UserInfo(name="alex1")
# session.add(obj1)

# session.add_all([
#     UserInfo(name='alex2'),
#     UserInfo(name='alex3')
# ])

# 提交事务
session.commit()
# 关闭session
session.close()
