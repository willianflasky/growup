#!/usr/bin/python
# -*- coding:utf-8 -*-

from rest_framework import  serializers
from django.contrib.auth.models import User
from asset import models

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('url', 'user', 'token', 'name')

# Serializers define the API representation.
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Asset
        depth = 2
        fields = ('url', 'name', 'sn', 'asset_type','status','admin','manufactory')

class ManufactorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufactory
        fields = ('url', 'manufactory', 'memo')

class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventLog
        fields = ('id', 'user', 'name', 'event_type', 'detail', 'asset', 'date', 'memo')
