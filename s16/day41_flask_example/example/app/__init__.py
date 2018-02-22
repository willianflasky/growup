#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from flask import Flask

from flask_session import Session
from auth.auth import Auth

from .views.account import account
from .views.user import user
from .views.main import main


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'sdiusdfsdf'
    # 设置配置文件
    app.config.from_object('settings.DevelopmentConfig')

    # 注册蓝图
    app.register_blueprint(account)
    app.register_blueprint(user)
    app.register_blueprint(main)

    # 注册组件
    # Session(app)
    Auth(app)

    return app
