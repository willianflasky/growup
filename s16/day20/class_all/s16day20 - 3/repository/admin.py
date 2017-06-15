from django.contrib import admin
from repository import models

admin.site.register(models.UserInfo)
admin.site.register(models.Comment)
admin.site.register(models.Favor)
admin.site.register(models.News)
admin.site.register(models.NewsType)
