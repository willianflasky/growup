#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/', views.index),
]
