#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

from sqlalchemy import create_engine,and_,or_,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,DateTime
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine("mysql+pymysql://root:123456@192.168.3.16:3306/db2", max_overflow=5)
Base=declarative_base()

UserProfile2HostUser=Table('userprofile_2_hostuser',Base.metadata,
                           Column('userprofile_id',ForeignKey('user_profile.id'),primary_key=True),
                           Column('hostuser_id',ForeignKey('host_user.id'),primary_key=True)
                           )

class Host(Base):
    __tablename__='host'
    id=Column(Integer,primary_key=True,autoincrement=True)
    hostname=Column(String(64),unique=True,nullable=False)
    ip_addr=Column(String(128),unique=True,nullable=False)
    port=Column(Integer,default=22)

    def __repr__(self):
        return "<id=%s,hostname=%s,ip_addr=%s,port=%s>"%(self.id,self.hostname,self.ip_addr,self.port)

class HostUser(Base):
    __tablename__='host_user'
    id=Column(Integer,primary_key=True)
    AuthTypes=[
        (u'ssh-passwd',u'SSH/Password'),
        (u'ssh-key',u'SSH/KEY'),
    ]
    auth_type=Column(String(64))
    username=Column(String(64),unique=True,nullable=False)
    password=Column(String(255))
    host_id=Column(Integer,ForeignKey('host.id'))

    #__table_args__ = (UniqueConstraint('host_id','username',name='_host_username_uc'))
    host = relationship('Host',backref='uu')

class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer,primary_key=True)
    username = Column(String(64),unique=True,nullable=False)
    password = Column(String(255),nullable=False)

    host_list = relationship('HostUser',secondary=UserProfile2HostUser,backref='userprofile')

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

Session=sessionmaker(bind=engine)
session=Session()
ret=session.query(Host.hostname).filter(Host.hostname=='willian').all()
print(ret)
# obj=session.query(HostUser.username,HostUser.password,Host.hostname,Host.port).join(Host).filter(HostUser.id==1).first()
# print(obj)

# obj=session.query(UserProfile).filter(username='input',password='input').first()
# if not obj: