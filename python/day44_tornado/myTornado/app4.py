#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/18 下午9:00
__author__ = "willian"

import tornado.ioloop
from tornado.web import RequestHandler
from session_code import SessionFactory


class SessionHandler(object):
    def initialize(self, *args, **kwargs):
        cls = SessionFactory.get_session()
        self.session = cls(self)


class IndexHandler(SessionHandler, RequestHandler):
    def get(self, *args, **kwargs):
        user = self.session['user']
        if user:
            self.write("welcome ")
        else:
            self.redirect("/login")


class LoginHandler(SessionHandler, RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        user = self.get_argument('user')
        pwd = self.get_argument('pwd')
        if user == 'alex' and pwd == "123":
            self.session['user'] = user
            self.redirect("/index")
        else:
            self.render('login.html')


class LogoutHandler(SessionHandler, RequestHandler):
    def get(self):
        del self.session['user']
        self.render('login.html')


# 配置文件
settings = {
    'template_path': "templates",
    'static_path': "static",
    'static_url_prefix': "/static/",
    "cookie_secret": 'google',
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
], **settings)

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
