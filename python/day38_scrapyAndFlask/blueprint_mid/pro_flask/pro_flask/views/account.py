#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from flask import request

# 创建Blueprint
account = Blueprint('account', __name__)


# 写视图和路由
@account.route('/login.html', methods=['GET', "POST"])
def login():
    return render_template('login.html')
