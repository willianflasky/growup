#!/usr/bin/env python
#-*- coding: utf-8 -*-
# by Wendy

from django.conf.urls import url,include
from django.contrib import admin
from testform import views

urlpatterns = [
    url(r'test$', views.customerform),
]
