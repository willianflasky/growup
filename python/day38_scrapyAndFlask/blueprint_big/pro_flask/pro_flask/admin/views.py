#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import admin


# 视图和路由
@admin.route('/index')
def index():
    return 'Admin.Index'