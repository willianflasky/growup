#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, redirect
from utils.pool.sqlhelper import SQLHelper

main = Blueprint('main', __name__)


@main.route('/index')
def index():
    with SQLHelper() as helper:
        user_list = helper.fetchall("select * from users", [])
    return render_template('index.html', user_list=user_list)
