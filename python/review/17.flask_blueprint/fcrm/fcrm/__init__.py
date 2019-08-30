#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/1/21 下午5:14
__author__ = "willian"

from flask import Flask
from .views import account
from .views import order

app = Flask(__name__)

app.register_blueprint(account.account)
app.register_blueprint(order.order)
