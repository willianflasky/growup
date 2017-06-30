
from django.conf.urls import url, include
from django.contrib import admin
# from MadKing import views

from asset import views
urlpatterns = [

    url(r'report/asset_with_no_asset_id/$', views.asset_with_no_asset_id),

]