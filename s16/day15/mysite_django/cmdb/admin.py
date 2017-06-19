from django.contrib import admin

# Register your models here.


from cmdb import models

admin.site.register(models.userinfo)
admin.site.register(models.usertype)


