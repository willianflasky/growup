#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^do-favor/', views.do_favor),

]
