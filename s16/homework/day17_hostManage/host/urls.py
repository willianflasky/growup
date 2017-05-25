#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django.conf.urls import url
from host import views
urlpatterns = [
    url(r'^$', views.host, name='HOST'),
    url(r'^login/', views.login, name='LOGIN'),
    url(r'^logout/', views.logout, name='LOGOUT'),
    url(r'^edit/', views.edit, name='EDIT'),
]