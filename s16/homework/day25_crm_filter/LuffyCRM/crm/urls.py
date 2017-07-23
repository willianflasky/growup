#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


from django.conf.urls import url,include
from crm import views
urlpatterns = [
    url(r'^customer_list/$', views.customer_list, name="customer_list"),
    url(r'^need_followup/$', views.need_followup, name="need_followup"),
]
