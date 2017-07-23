#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django.conf.urls import url,include

from luffyAdmin import views
urlpatterns = [
    url(r'^$', views.app_index),
    url(r'(\w+)/(\w+)/$', views.model_table_list, name="model_table_list"),
]
