#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.forms import Form
from django.forms import fields

class LoginForm(Form):
    username = fields.CharField()
    pwd = fields.CharField()