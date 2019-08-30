#!/usr/bin/env python
#-*- coding: utf-8 -*-
# by Wendy

from django.conf import settings

for app_name in settings.INSTALLED_APPS:
    try:
        #导入每个app的crm_admin文件
        #print("%s.%s"%(app_name,'crm_admin----'))
        __import__( "%s.%s" %(app_name,'crm_admin') )

    except ImportError:
        pass