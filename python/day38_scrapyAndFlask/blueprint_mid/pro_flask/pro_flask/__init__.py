#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask

# 指定静态和模板目录
app = Flask(__name__, template_folder='templates', static_folder='statics', static_url_path='/static')

# app引入
from .views.account import account
from .views.blog import blog
from .views.user import user

# app注册进blueprint
app.register_blueprint(account)
app.register_blueprint(blog)
app.register_blueprint(user)
