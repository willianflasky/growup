


print("------------crm luffyadmin.py")
from crm import models
from luffyAdmin.admin_base import  site,BaseAdmin


class CustomerAdmin(BaseAdmin):
    list_display = ['name','qq','consultant','source','status']
    list_filter = ['consultant','source','status']
    list_per_page = 1


class CourseAdmin(BaseAdmin):
    list_display = ['name','period','price']

site.register(models.Customer,CustomerAdmin)
site.register(models.Course,CourseAdmin)
site.register(models.ClassList)