#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='s13')
cursor = conn.cursor(cursor=pymysql.cursor.DictCursor)    #字典的方式获取数据
cursor.execute('select * from t10')

#获取数据量
row=cursor.fetchone()
row=cursor.fetchmany(3)
row=cursor.fetchall()

#指针移动
#cursor.scroll(1,mode='relative')

conn.commit()
cursor.close()
conn.close()
