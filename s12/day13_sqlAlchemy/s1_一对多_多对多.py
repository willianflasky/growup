#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String,ForeignKey,UniqueConstraint,Index,Table
from sqlalchemy.orm import sessionmaker,relationship
engine=create_engine('mysql+pymysql://root:100200@192.168.3.6:3306/s13',max_overflow=5)

Base=declarative_base()

class Test(Base):
    __tablename__ = 'test'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))


#一对多
class Group(Base):
    __tablename__ = 'group'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    caption = Column(String(32))

    def __repr__(self):
        temp = "%s,%s"%(self.nid,self.caption)
        return temp

class User(Base):
    __tablename__ = 'user'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))
    group_id = Column(Integer,ForeignKey('group.nid'))
    group = relationship('Group',backref='uuu')

    def __repr__(self):
        temp="%s,%s,%s"%(self.nid,self.name,self.group_id)
        return temp

#多对多

class HostToHostUser(Base):
    __tablename__ ='host_to_host_user'
    nid=Column(Integer,primary_key=True,autoincrement=True)
    host_id=Column(Integer,ForeignKey('host.nid'))
    host_user_id=Column(Integer,ForeignKey('host_user.nid'))

    # host=relationship('Host',backref='h')
    # hostuser=relationship('HostUser',backref='u')


class Host(Base):
    __tablename__= 'host'
    nid= Column(Integer,primary_key=True,autoincrement=True)
    hostname=Column(String(32))
    port=Column(String(32))
    ip=Column(String(32))

    host_user=relationship('HostUser',secondary=HostToHostUser.__tablename__,backref='h')

class HostUser(Base):
    __tablename__ = 'host_user'
    nid=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(32))



def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

#init_db()

Session=sessionmaker(bind=engine)
session=Session()


#单表操作
#session.add(Group(caption='dba'))
#session.add(Group(caption='ddd'))
#session.commit()

#session.add_all([
#    User(name='alex1',group_id=1),
#    User(name='alex2',group_id=2),
#])
# #session.commit()

# ret=session.query(User).filter(User.name=='alex1').all()
# print(ret)
# ret=session.query(User).all()
# print(ret)
# obj=ret[0]
# print(obj.nid,obj.name,obj.group_id)

# ret=session.query(User.name).all()
# print(ret)

#连表操作
# sql=session.query(User.name,Group.caption).join(Group,isouter=True)
# print(sql)
# ret=session.query(User.name,Group.caption).join(Group,isouter=True).all()
# print(ret)


#新方式 正向查询
# ret = session.query(User).all()
# for obj in ret:
#     print(obj.nid,obj.name,obj.group_id,obj.group)

# 原始方式
# ret=session.query(User.name,Group.caption).join(Group,isouter=True).filter(Group.caption=='DBA').all()

#新方式 反向查询
# obj = session.query(Group).filter(Group.caption=='DBA').first()
# print(obj.nid)
# print(obj.caption)
# print(obj.uuu)

###多对多
# session.add_all([
#     Host(hostname='c1',port='22',ip='1.1.1.1'),
#     Host(hostname='c2',port='22',ip='1.1.1.2'),
#     Host(hostname='c3',port='22',ip='1.1.1.3'),
#     Host(hostname='c4',port='22',ip='1.1.1.4'),
#     Host(hostname='c5',port='22',ip='1.1.1.5'),
# ])
# session.commit()

# session.add_all([
#     HostUser(name='root'),
#     HostUser(name='db'),
#     HostUser(name='nb'),
#     HostUser(name='sb'),
# ])
# session.commit()

# session.add_all([
#     HostToHostUser(host_id=1,host_user_id=1),
#     HostToHostUser(host_id=1,host_user_id=2),
#     HostToHostUser(host_id=1,host_user_id=3),
#     HostToHostUser(host_id=2,host_user_id=2),
#     HostToHostUser(host_id=2,host_user_id=4),
#     HostToHostUser(host_id=2,host_user_id=3),
# ])
# session.commit()


#原始方式
"""
#获取主机1的所有用户
#1.根据主机名找到主机ID
host_obj=session.query(Host).filter(Host.hostname=='c1').first()
print(host_obj.nid)
#2.根据主机ID找到所有用户ID
host_2_host_user=session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id==host_obj.nid).all()
print(host_2_host_user)
r=zip(*host_2_host_user)
#3.根据用户ID找到所有用户
users=session.query(HostUser.name).filter(HostUser.nid.in_(list(r)[0])).all()
print(users)
"""

#新方法
#先反向查找,再正向查找
# host_obj=session.query(Host).filter(Host.hostname=='c1').first()
# #第三张表的对象
# print(host_obj.h)
#
# for item in host_obj.h:
#     print(item.hostuser.name)

host_obj=session.query(Host).filter(Host.hostname=='c1').first()

for item in host_obj.host_user:
    print(item.name)