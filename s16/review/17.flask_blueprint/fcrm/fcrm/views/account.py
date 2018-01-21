#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/1/21 下午5:18
__author__ = "willian"

from flask import Blueprint, render_template

account = Blueprint('account', __name__)


@account.route("/login")
def login():
    return render_template("login.html")
