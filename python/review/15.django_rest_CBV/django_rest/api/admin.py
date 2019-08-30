from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api import models

# Register your models here.

admin.site.register(models.Book)
admin.site.register(models.Publisher)
admin.site.register(models.Author)
