#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


from django import template
from django.utils.safestring import mark_safe
from django.template.base import Node, TemplateSyntaxError

register = template.Library()

@register.filter
def f1(value,arg):
    return value + "666" + arg



@register.simple_tag
def f2(s1,s2,s3,s4):
    return s1+s2+s3+s4


@register.filter
def f3(value):
    if value == "V":
        return True
    else:
        return False