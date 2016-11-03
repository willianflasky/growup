#!/usr/bin/env python       
import MySQLdb 
  
class DB(): 
    def __init__(self, DB_HOST, DB_PORT, DB_USER, DB_PWD, DB_NAME): 
        self.DB_HOST = DB_HOST 
        self.DB_PORT = DB_PORT 
        self.DB_USER = DB_USER 
        self.DB_PWD = DB_PWD 
        self.DB_NAME = DB_NAME 
          
        self.conn = self.getConnection() 
  
    def getConnection(self): 

        return MySQLdb.Connect( 
                           host=self.DB_HOST,
                           port=self.DB_PORT,
                           user=self.DB_USER,
                           passwd=self.DB_PWD, 
                           db=self.DB_NAME,
                           charset='utf8'
                           ) 
  
    def query(self, sqlString): 
        cursor=self.conn.cursor() 
        cursor.execute(sqlString) 
        returnData=cursor.fetchall() 
        cursor.close() 
        self.conn.close() 
        return returnData 
      
    def update(self, sqlString): 
        cursor=self.conn.cursor() 
        cursor.execute(sqlString) 
        self.conn.commit() 
        cursor.close() 
        self.conn.close() 
  
if __name__=="__main__": 
    db=DB('1.1.1.1',3306,'zabbix','zabbix','zabbix') 
    ret=db.query("show tables;")
    for table in ret:
        print(table)
