#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/5 下午5:55
__author__ = "willian"
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.shortcuts import HttpResponse


class RbacMiddleware(MiddlewareMixin):

    def process_request(self, request):
        current_url = request.path_info
        can_do_url = request.session[settings.SESSION_PERMISSION_URL_KEY]

        if current_url not in can_do_url and current_url != "/login.html/":
            return HttpResponse("403")
