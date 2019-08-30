#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, request, render_template, redirect, session, current_app
from utils.pool.sqlhelper import SQLHelper

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        with SQLHelper() as helper:
            result = helper.fetchone('select * from users where name=%s and pwd = %s',
                                     [request.form.get('user'), request.form.get('pwd'), ])

        if result:
            current_app.auth_manager.login(result['name'])
            return redirect('/index')
        else:
            return render_template('login.html')
