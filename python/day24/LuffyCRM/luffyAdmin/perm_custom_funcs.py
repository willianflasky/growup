#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


def only_view_own_customers(request, *args, **kwargs):

    consultant_id = request.GET.get('consultant')
    if consultant_id:
        consultant_id = int(consultant_id)

    if consultant_id == request.user.id:
        return True
    else:
        return False
