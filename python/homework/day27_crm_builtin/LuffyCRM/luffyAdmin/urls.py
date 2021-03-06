#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django.conf.urls import url,include

from luffyAdmin import views
urlpatterns = [
    url(r'^$', views.app_index),
    url(r'^(\w+)/(\w+)/$', views.model_table_list, name="model_table_list"),
    url(r'^(\w+)/(\w+)/(\d+)/change/$', views.table_obj_change, name="table_obj_change"),
    url(r'^(\w+)/(\w+)/(\d+)/delete/$', views.table_object_del, name="object_del"),
    url(r'^(\w+)/(\w+)/add/$', views.table_obj_add, name="table_obj_add"),
]
