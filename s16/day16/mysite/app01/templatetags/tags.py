#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django import template

register = template.Library()


@register.filter
def mul(x, y):
    ret = 1
    for i in eval(y):
        ret *= i
    return ret * x


@register.simple_tag
def mul2(x, y, z):
    return x * y * z
