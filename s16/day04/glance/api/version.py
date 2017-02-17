#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


def create_resource(conf):
    print('from version.py: ',conf)


from ..api import policy
policy.get()