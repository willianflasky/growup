#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/17 下午8:31
__author__ = "willian"
from tornado.web import RequestHandler
import time


class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html", msg="")

    def post(self, *args, **kwargs):
        user = self.get_argument('user')
        pwd = self.get_argument('pwd')

        if user == 'alex' and pwd == '123':
            t = time.time() + 300
            self.set_cookie("username", user, expires=t)
            self.redirect("/seed.html")
        else:
            self.render('login.html', msg="user or password error!")


class SeedHandler(RequestHandler):
    def get(self, *args, **kwargs):
        name = self.get_cookie('username')
        if not name:
            self.redirect('/login.html')
            return None
        self.write('welcome login')

    def post(self, *args, **kwargs):
        pass


class LogoutHandler(RequestHandler):
    def get(self):
        self.clear_cookie('username')
