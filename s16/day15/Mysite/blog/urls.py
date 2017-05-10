
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [

    url(r'^blog/', views.index),

    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/([0-9]{4})/$', views.year_archive),  # year_archive(request,2009)

    # url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),# month_archive(request,2008,12)
    url(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    # month_archive(request,year=2008,month=12)

    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),



]
