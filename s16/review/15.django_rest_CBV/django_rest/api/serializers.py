#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2017/12/6 下午3:58
__author__ = "willian"
from .models import *
from rest_framework import serializers


# 和FormModel一样,定义 ModelSerializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
