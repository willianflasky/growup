#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


from django.conf.urls import url, include
from crm import views
urlpatterns = [
    url(r'^customer_list/$', views.customer_list, name="customer_list"),
    url(r'^customer_list/add/$', views.customer_add, name="customer_add"),
    url(r'^customer_list/(\d+)/change/$', views.customer_change, name="customer_change"),
    url(r'^need_followup/$', views.need_followup, name="need_followup"),
]
