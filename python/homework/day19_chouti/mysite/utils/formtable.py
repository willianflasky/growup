#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django.forms import Form
from django.forms import fields


class LoginForm(Form):
    user = fields.CharField(error_messages={'required': "用户名不能为空"})
    pwd = fields.CharField(error_messages={'required': "密码不能为空"})


class LinkForm(Form):
    title = fields.CharField(required=True, error_messages={'required': "标题不能为空"})
    content = fields.CharField(required=True, error_messages={'required': "摘要不能为空"})
    url = fields.CharField(required=True, error_messages={'required': "URL路径不能为空"})
    news_type_id = fields.IntegerField()


