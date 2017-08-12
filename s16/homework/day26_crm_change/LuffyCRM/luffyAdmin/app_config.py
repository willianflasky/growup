#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

# 通过settings拿到app
# 把app下面的luffy_admin压进来,如果没有抛异常就不压入.
from django.conf import settings

for app_name in settings.INSTALLED_APPS:
    try:
        __import__("%s.%s" % (app_name, "luffy_admin"))

    except ImportError:
        pass