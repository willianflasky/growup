#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


from django.conf.urls import url
from web import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^editor/', views.editor),
    url(r'^upload_img/', views.upload_img),
    url(r'^news/([a-z]+)/', views.qu),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^favor/', views.favor),
    url(r'^comment/', views.comment),
    url(r'^check_code/', views.check_code),
]
