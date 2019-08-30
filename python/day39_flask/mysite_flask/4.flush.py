#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/1/18 下午7:28
__author__ = "willian"

from flask import Flask, flash, redirect, get_flashed_messages

app = Flask(__name__, template_folder="templates", static_url_path="/static")

app.secret_key = 'xx'


@app.route('/user', methods=['get', 'post'])
def user():
    v = get_flashed_messages()
    print(v)
    return "from user : %s" % v


@app.route('/useradd')
def useradd():
    flash("添加成功")
    return redirect("/user")


if __name__ == '__main__':
    app.run()
