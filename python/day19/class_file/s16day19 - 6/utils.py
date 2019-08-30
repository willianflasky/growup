#!/usr/bin/python
# -*- coding:utf-8 -*-


class BaseReponse:
    def __init__(self):
        self.status = False
        self.data = None
        self.error = None