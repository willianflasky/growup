#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,UniqueConstraint,Index,Table
from sqlalchemy.orm import sessionmaker,relationship
engine=create_engine('mysql+pymysql://root:100200@192.168.3.6:3306/db1',max_overflow=5)

Base=declarative_base()

#单表
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (
    UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

    def __repr__(self):
        return "%s-%s" %(self.id, self.name)


#一对多
class Favor(Base):
    __tablename__ = 'favor'
    nid= Column(Integer,primary_key=True)
    caption = Column(String(50),default='red',unique=True)

    def __repr__(self):
        return "%s - %s"%(self.nid,self.caption)

class Person(Base):
    __tablename__ = 'person'
    nid= Column(Integer,primary_key=True)
    name= Column(String(32),index=True,nullable=True)
    favor_id=Column(Integer,ForeignKey('favor.nid'))

    favor = relationship('Favor',backref='pers')

    def __repr__(self):
        return "%s - %s"%(self.nid,self.name)

#多对多

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True,nullable=False)
    port = Column(Integer,default=22)

class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)

class ServerToGroup(Base):
    __tablename__= 'servertogroup'
    nid=Column(Integer,primary_key=True,autoincrement=True)
    server_id=Column(Integer,ForeignKey('server.id'))
    group_id=Column(Integer,ForeignKey('group.id'))


def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)


#init_db()

Session=sessionmaker(bind=engine)
session=Session()

#增加
# obj=Favor(caption='red')
# session.add(obj)
# session.commit()
#批量增加
# session.add_all([
#     # Favor(caption='yellow'),
#     # Favor(caption='green'),
#     Favor(caption='blue'),
# ])
# session.commit()

#删除
# ret=session.query(Favor).filter(Favor.nid == 4).delete()
# print(ret)
# session.commit()

#改
#session.query(Favor).filter(Favor.nid == 44).update({'nid':'4'})
#session.query(Favor).filter(Favor.caption == 'red').update({Favor.caption:Favor.caption + "other"},synchronize_session=False) #string拼接
# session.query(Favor).filter(Favor.nid == '1').update({Favor.nid:Favor.nid + 4},synchronize_session="evaluate") #num计算
# session.commit()

#查
# ret=session.query(Favor).all()
# ret=session.query(Favor.nid,Favor.caption).all()
# ret=session.query(Favor.caption).filter_by(caption='red').all()
# ret=session.query(Favor.caption).filter_by(caption='red').first()
# print(ret)

#其它查询 filter and filter_by
# ret = session.query(Favor).filter_by(caption='red').all()
# ret = session.query(Person).filter(Person.nid==6,Person.name=='mother').all()
# ret = session.query(Favor).filter(Favor.nid.between(1,3)).all()
# ret = session.query(Favor).filter(Favor.nid.in_([1,2,4])).all()
# ret = session.query(Favor).filter(~Favor.nid.in_([1,2,4])).all()
# ret = session.query(Favor).filter(Favor.nid.in_(session.query(Favor.nid).filter_by(caption='blue'))).all()
from sqlalchemy import and_,or_
# ret = session.query(Favor).filter(and_(Favor.nid>3,Favor.caption == 'blue')).all()
# ret = session.query(Favor).filter(or_(Favor.nid>3,Favor.caption == 'blue')).all()
# ret = session.query(Favor).filter(or_(Favor.nid<2,and_(Favor.caption=='blue',Favor.nid >3),Favor.nid !="")).all()

#通配符
# ret = session.query(Favor).filter(Favor.caption.like('%e')).all()
# ret = session.query(Favor).filter(~Favor.caption.like('%e')).all()

#限制
# ret = session.query(Favor)[1:3]

#排序 asc正排,desc倒排
# ret = session.query(Favor).order_by(Favor.caption.desc()).all()
# ret = session.query(Favor).order_by(Favor.nid.asc()).all()

#分组
from sqlalchemy.sql import func
# ret = session.query(Favor).group_by(Favor.nid).all()
# ret = session.query(
#     func.sum(Favor.nid)
# ).group_by(Favor.caption).all()

# ret = session.query(
#     func.max(Favor.nid),
# ).group_by(Favor.caption).having(func.min(Favor.nid) > 2).all()

#连表
# ret = session.query(Users,Favor).filter(Users.id == Favor.nid).all()
# ret = session.query(Person).join(Favor).all()       #inner join
# ret = session.query(Person).join(Favor,isouter=True).all()  #left join

#组合
# q1 = session.query(Users.name).filter(Users.id > 2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union(q2).all()
#
# q1 = session.query(Users.name).filter(Users.id >2)
# q2 = session.query(Favor.caption).filter(Favor.nid < 2)
# ret = q1.union_all(q2).all()

