#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

user = Blueprint('user', __name__)


# 写视图和路由
@user.route('/user.html', methods=['GET', "POST"])
def login():
    return render_template('user.html')
