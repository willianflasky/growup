#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/4 下午11:36
__author__ = "willian"
from django.conf import settings
from .. import models


def init_permission(request, user_obj):
    permission_item_list = user_obj.roles.values('permissions__title', 'permissions__url',
                                                 'permissions__menu_id').distinct()
    # 保存所有的用户权限 URL
    permission_url_list = []
    # 保存当前用户有权访问的URL且需要在菜单上显示
    permission_menu_list = []
    for item in permission_item_list:
        permission_url_list.append(item['permissions__url'])
        if item['permissions__menu_id']:
            tmp = {'title': item['permissions__title'], 'url': item['permissions__url'],
                   'menu_id': item['permissions__menu_id']}
            permission_menu_list.append(tmp)

    menu_list = list(models.Menu.objects.values('caption', 'parent_id'))

    request.session[settings.SESSION_PERMISSION_URL_KEY] = permission_url_list
    request.session[settings.SESSION_PERMISSION_MENU_URL_KEY] = {
        settings.PERMISSION_URL_KEY: permission_menu_list,
        settings.ALL_MENU_KEY: menu_list
    }
