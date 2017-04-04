#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import flask


def f1(header, body):
    return "from f1"


def f2(header, body):
    return "from f2"

routers = [
    ('/index.html', f1),
    ('/login.html', f2),
]

obj = flask.Flask(routers)
obj.run()
