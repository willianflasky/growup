#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.forms import Form
from django.forms import fields

class LoginForm(Form):
    username = fields.CharField(min_length=6,max_length=18)
    pwd = fields.CharField(min_length=12)