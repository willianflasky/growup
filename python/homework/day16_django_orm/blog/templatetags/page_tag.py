#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django import template
from django.utils.html import format_html
register = template.Library()


@register.simple_tag
def guess_page(current_page, loop_num):
        offset = abs(current_page-loop_num)
        if offset < 3:
            if current_page == loop_num:
                page_ele = '<li class="active"><span ><a href="?p=%s">%s</a></span></li>' % (loop_num, loop_num)
            else:
                page_ele = '<li><span class=""><a href="?p=%s">%s</a></span></li>' % (loop_num, loop_num)
            return format_html(page_ele)
        else:
            return ""
