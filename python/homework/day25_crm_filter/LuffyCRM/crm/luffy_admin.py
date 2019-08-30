#!/usr/bin/env python

from crm import models
from luffyAdmin.admin_base import site, BaseAdmin

print("------------crm luffy_admin.py")


# 自定义customer表的管理类
class CustomerAdmin(BaseAdmin):
    list_display = ['name', 'qq', 'consultant', 'source', 'status']
    list_filter = ['consultant', 'source', 'status', 'tags']
    list_per_page = 10
    search_fields = ['email', ]


# 自定义course表的管理类
class CourseAdmin(BaseAdmin):
    list_display = ['name', 'period', 'price']
    list_per_page = 10


class ClassListAdmin(BaseAdmin):
    list_display = ['course', 'branch']
    list_per_page = 10


# 注册,关联表和管理类,没有指定使用基类
site.register(models.Customer, CustomerAdmin)
site.register(models.Course, CourseAdmin)
site.register(models.ClassList, ClassListAdmin)
