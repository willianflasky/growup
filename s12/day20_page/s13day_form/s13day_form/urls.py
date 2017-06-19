"""s13day_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^add/',views.add_user_type),
    url(r'^add_boy/',views.add_boy),
    url(r'^add_girl/',views.add_girl),
    url(r'^boy_to_girl/',views.boy_to_girl),
    url(r'^md/',views.md),
    url(r'^cache/',views.cache),
    url(r'^page/',views.page),
    url(r'^page1/',views.page1),
    url(r'^page2/',views.page2),
    url(r'^user_list/',views.user_list),
]
