from django.shortcuts import HttpResponse


print("------------crm luffyadmin.py")
from crm import models
from luffyAdmin.admin_base import  site,BaseAdmin

class CustomerAdmin(BaseAdmin):
    list_display = ['id','qq','name','consultant','source','status']
    list_filter = ['consultant','source','status']
    list_per_page = 2
    search_fields = ['qq','source__name']
    filter_horizontal = ['tags','consult_courses']
    actions = ['enroll']
    readonly_fields = ['name', 'qq','tags','consultant']
    def enroll(self,request,querysets):
        print("-enroll   ",request,querysets)
        querysets.update(status=0)
        return HttpResponse("to another page")



class CourseAdmin(BaseAdmin):
    list_display = ['name','period','price']




site.register(models.Customer,CustomerAdmin)
site.register(models.Course,CourseAdmin)
site.register(models.ClassList)
site.register(models.Account)