#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/17 下午8:34
__author__ = "willian"


from tornado.web import RequestHandler


class SeedHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.request
        self.render('hello world')

    def post(self, *args, **kwargs):
        pass