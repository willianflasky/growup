#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/users')
def users():
    return 'users'
