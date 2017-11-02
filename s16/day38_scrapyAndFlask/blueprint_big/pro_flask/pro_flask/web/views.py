#!/usr/bin/env python
# -*- coding:utf-8 -*-

from . import web


@web.route('/index')
def index():
    return 'Web.Index'