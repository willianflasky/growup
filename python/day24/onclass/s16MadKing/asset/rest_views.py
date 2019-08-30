#!/usr/bin/python
# -*- coding:utf-8 -*-

from rest_framework import viewsets
from django.contrib.auth.models import User
from asset.rest_searilizers import UserSerializer,AssetSerializer,ManufactorySerializer, \
    UserProfileSerializer
from asset import models

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = models.Asset.objects.all()
    serializer_class = AssetSerializer

class ManufactoryViewSet(viewsets.ModelViewSet):
    queryset = models.Manufactory.objects.all()
    serializer_class = ManufactorySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = UserProfileSerializer

