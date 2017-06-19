#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


from django.conf.urls import url
from django.contrib import admin
from cmdb import views


urlpatterns = [
    url(r'^index/(\d+)/', views.index),
    url(r'^detail/(\d+)/', views.detail),
]
