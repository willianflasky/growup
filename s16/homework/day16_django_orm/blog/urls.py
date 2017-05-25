#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='LOGIN'),
    url(r'^$', views.blog),
    url(r'^logout/$', views.logout),
    url(r'^detail/(?P<num>\d+)/$', views.detail),
    url(r'^append/$', views.append, name='APPEND'),
]