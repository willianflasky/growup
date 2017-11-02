#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template

blog = Blueprint('blog', __name__)


# 写视图和路由
@blog.route('/blog.html', methods=['GET', "POST"])
def login():
    return render_template('blog.html')
