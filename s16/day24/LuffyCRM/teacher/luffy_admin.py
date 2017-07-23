#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

print("------------teacher luffyadmin.py")
from teacher import models
from luffyAdmin.admin_base import BaseAdmin, site


class TeacherTestAdmin(BaseAdmin):
    list_display = ['name']


site.register(models.TeacherTest,TeacherTestAdmin)
