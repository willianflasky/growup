"""LuffyCRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from crm import views

# restful api =================================
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from crm.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        depth = 2
        fields = ('url', 'username', 'email', 'is_staff')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        depth = 2
        fields = ('name', 'qq', 'weixin', 'phone', 'email', 'source', 'content', 'status', 'tags', 'consultant', 'date',
                  'consult_courses', 'referral_from',
                  )


class ClassListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClassList
        depth = 2
        fields = ('course', 'branch', 'semester', 'contract', 'class_type', 'max_student_num', 'teachers', 'start_date',
                  'end_date')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ClassListViewSet(viewsets.ModelViewSet):
    queryset = ClassList.objects.all()
    serializer_class = ClassListSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Customer', CustomerViewSet)
router.register(r'ClassList', ClassListViewSet)
# =================================================

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^logout/', views.web_logout, name='LOGOUT'),
    url(r'^login/', views.web_login, name='LOGIN'),
    # restful api  ======================================
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # ===================================================
]


