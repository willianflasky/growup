#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2017/12/3 上午9:29
__author__ = "willian"

from django.core.signals import request_finished
from django.dispatch import receiver


# 信号
@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("request finished")
    print(sender, kwargs)
