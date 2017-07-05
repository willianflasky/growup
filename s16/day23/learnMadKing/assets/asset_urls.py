#!/usr/bin/env python
#-*- coding: utf-8 -*-
# by Wendy

from django.conf.urls import include, url
from assets import views

urlpatterns = [
    url(r'report/asset_with_no_asset_id/$', views.asset_with_no_asset_id, name='acquire_asset_id'),
    url(r'report/$', views.asset_report, name='asset_report'),
]