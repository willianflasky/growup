#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/2/22 下午12:54
__author__ = "willian"
import time
import threading
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from models import UserInfo, Person, Hobby

engine = create_engine("mysql+pymysql://s6:s6@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

session = Session()

# 条件
# ret = session.query(UserInfo).filter_by(name='alex099').all()
# ret = session.query(UserInfo).filter(UserInfo.id > 1, UserInfo.name == 'alex099').all()
# ret = session.query(UserInfo).filter(UserInfo.id.between(1, 3), UserInfo.name == 'alex099').all()
# ret = session.query(UserInfo).filter(UserInfo.id.in_([1, 3, 4])).all()
# ret = session.query(UserInfo).filter(~UserInfo.id.in_([1, 3, 4])).all()
# ret = session.query(UserInfo).filter(UserInfo.id.in_(session.query(UserInfo.id).filter_by(name='wupeiqi'))).all()

from sqlalchemy import and_, or_
# ret = session.query(UserInfo).filter(and_(UserInfo.id > 3, UserInfo.name == 'alex099')).all()
# ret = session.query(UserInfo).filter(or_(UserInfo.id < 2, UserInfo.name == 'wupeiqi')).all()
# ret = session.query(UserInfo).filter(
#     or_(
#         UserInfo.id < 2,
#         and_(UserInfo.name == 'alex099', UserInfo.id > 3),
#         UserInfo.name != "",
#     )).all()


# 通配符
# ret = session.query(UserInfo).filter(UserInfo.name.like('alex%')).all()
# ret = session.query(UserInfo).filter(~UserInfo.name.like('ale%')).all()
#
# # 限制
# ret = session.query(UserInfo)[1:2]
#
# # 排序
# ret = session.query(UserInfo).order_by(UserInfo.name.desc()).all()
# ret = session.query(UserInfo).order_by(UserInfo.name.desc(), UserInfo.id.asc()).all()
#
# # 分组
from sqlalchemy.sql import func

#
# ret = session.query(UserInfo).group_by(UserInfo.name).all()
# ret = session.query(
#     func.max(UserInfo.id),
#     func.sum(UserInfo.id),
#     func.min(UserInfo.id)).group_by(UserInfo.name).all()
#
# ret = session.query(
#     func.max(UserInfo.id),
#     func.sum(UserInfo.id),
#     func.min(UserInfo.id)).group_by(UserInfo.name).having(func.min(UserInfo.id) > 2).all()
#
# # 连表
#
# ret = session.query(Person, Hobby).filter(Person.hobby_id == Hobby.id).all()
#
# ret = session.query(Person).join(Hobby).all()
#
# ret = session.query(Person).join(Hobby, isouter=True).all()
#
#
# # 组合
# q1 = session.query(Person.name).filter(Person.nid > 2)
# q2 = session.query(Hobby.caption).filter(Hobby.id < 2)
# ret = q1.union(q2).all()
#
# q1 = session.query(Person.name).filter(Person.nid > 2)
# q2 = session.query(Hobby.caption).filter(Hobby.id < 2)
# ret = q1.union_all(q2).all()

# print(ret)

session.close()
