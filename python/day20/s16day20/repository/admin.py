from django.contrib import admin
from repository.models import *

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Comment)
admin.site.register(Favor)
admin.site.register(News)
admin.site.register(NewsType)
