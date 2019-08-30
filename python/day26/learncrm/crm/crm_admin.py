#!/usr/bin/env python
#-*- coding: utf-8 -*-
# by Wendy

print("------------crm crmAdmin.py")
from crm import models
from crmAdmin.admin_base import site,BaseAdmin

class CustomerAdmin(BaseAdmin):
    list_display = ['id','name','qq','consultant','source','status']
    list_filter = ['consultant','source','status']
    list_per_page = 8
    search_fields = ['qq','source__name']
    filter_horizontal = ['tags', 'consult_courses']
    actions = ['status', ]


    def status(self, request, querysets):
        print("action 配置")
        # 状态修改
        querysets.update(status=2)

    status.short_description = "Status状态修改成报名"


# 换个名字
# 这个函数的3个参数
# 1、类本身
# 2、request
# 3、你所选中的数据



class CourseAdmin(BaseAdmin):
    list_display = ['name','period','price']

site.register(models.Customer,CustomerAdmin)
site.register(models.Course,CourseAdmin)
site.register(models.ClassList)