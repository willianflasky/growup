#!/usr/bin/env python

from day5.dj.config import settings

def db_auth(configs):
    if configs.DATABASES['user']=='root' and configs.DATABASES['password']=='123':
        print('auth passed')
        return True
    else:
        print('db login error....')

def select(table,column):
    if db_auth(settings):
        if table == 'user':
            user_info = {

                "001":['alex',22,'engineer'],
                "002":['lognge',43,'chef,engineer'],
                "003":['xiaoyun',23,'13engineer']
            }
        return user_info