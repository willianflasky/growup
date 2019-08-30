#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2017/12/7 下午5:48
__author__ = "willian"

from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser()
