#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from .admin import admin
from .web import web

app = Flask(__name__)
app.debug = True

# app注册，同时指定url前缀，和django include一样；
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(web)
