from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Menu)
admin.site.register(models.Permission)
admin.site.register(models.Role)
admin.site.register(models.UserInfo)
