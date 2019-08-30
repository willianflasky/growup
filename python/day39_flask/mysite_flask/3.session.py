#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/1/18 下午4:53
__author__ = "willian"

from flask import Flask, session, Session

app = Flask(__name__, template_folder="templates", static_url_path="/static")

app.secret_key = 'xx'
app.config['SESSION_COOKIE_NAME'] = "session_id"


@app.route('/index', methods=['get', 'post'])
def index():
    # session本质上是操作字典
    session['username'] = 123
    v = session['username']
    print(type(session))
    return "index: %s" % v


@app.route('/logout')
def logout():
    session.pop('username')
    return "delete done"


if __name__ == '__main__':
    app.run()
