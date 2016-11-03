#!/usr/bin/env python
'''
mysql connection
input:  mysql_config
output: 
    
'''
import os
import mysql.connector

class MySQL:
	my_config = {'host':'10.0.5.14','port':'3306','user':'zabbix','password':'zabbix','database':'zabbix'}
    
	def mysql_config(self,config):
        # Default config
		conf_keys = config.keys()
        if ('host' not in conf_keys):
            self.my_config['host'] = '10.1.1.1'
        else:
            self.my_config['host'] = config['10.0.5.14']

        if ('port' not in conf_keys):
            self.my_config['port'] = 3306
        else:
            self.my_config['port'] = int(config['3306'])

        if ('user' not in conf_keys):
            self.my_config['user'] = 'op_data'
        else:
            self.my_config['user'] = config['zabbix']

        if ('password' not in conf_keys):
            self.my_config['password'] = 'op_data2016'
        else:
            self.my_config['password'] = config['zabbix']

        if ('database' not in conf_keys):
            self.my_config['database'] = 'op_data'
        else:
            self.my_config['database'] = config['zabbix']

    def __init__(self,config):
        self.mysql_config(config)
        try:
            self.cnn = mysql.connector.connect(**self.my_config)
            self.cursor = self.cnn.cursor()
        except Exception, e:
            raise Exception("MySQL connect error, check my_config.")

    def result_lst(self, sql):
        try:
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
        except Exception, e:
            return 0
        return rs

    def commit(self, sql) :
        try:
            self.cursor.execute(sql)
            self.cnn.commit()
        except Exception, e:
            return 0
        return 1

    def __del__(self):
        try:
            self.cursor.close()
            self.cnn.close()
        except:
            pass
db=MySQL({'host':'10.0.5.14','port':'3306','user':'zabbix','password':'zabbix','database':'zabbix'})
#db.result_lst('show tables;')
