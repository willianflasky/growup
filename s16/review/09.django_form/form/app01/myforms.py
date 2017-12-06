#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2017/11/23 下午8:32
__author__ = "willian"

from django import forms
from django.forms import Form, fields, widgets


class hosts_form(Form):
    ip = fields.CharField(label="地址", help_text="10.1.1.1", min_length=7, max_length=16,
                          error_messages={'required': "地址不能为这空",
                                          "min_length": "长度不能小于7",
                                          "max_length": "长度不能大于16",
                                          })
    port = fields.CharField(label="端口", help_text="22", max_length=6,
                            widget=widgets.Textarea
                            )
