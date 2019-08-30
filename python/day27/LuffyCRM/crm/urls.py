
from django.conf.urls import url,include
from crm import views
urlpatterns = [
    url(r'^customer_list/$', views.customer_list,name="customer_list"),
    url(r'^customer_list/(\d+)/change/$', views.customer_change,name="customer_change"),

]
