#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', views.login, name="LOGIN"),
    url(r'^logout/$', views.logout),
    url(r'^$', views.show_data),
    url(r'^add_books/$', views.add_books),
    url(r'^del_books/$', views.del_books),
    url(r'^edit_books/$', views.edit_books),
]
