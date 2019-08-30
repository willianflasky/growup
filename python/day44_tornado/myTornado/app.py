#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/17 下午8:28
__author__ = "willian"

import tornado.ioloop
import tornado.web
from controllers.account import LoginHandler, LogoutHandler, SeedHandler

# 配置文件
settings = {
    'template_path': "templates",
    'static_path': "static",
    'static_url_prefix': "/static/",
    'xsrf_cookies': True,
    "cookie_secret": 'google',
}

application = tornado.web.Application([
    (r"/login.html", LoginHandler, {}, "login"),
    (r"/logout.html", LogoutHandler),
    (r"/seed.html", SeedHandler),
], **settings)

if __name__ == '__main__':
    # 实例化socket对象
    application.listen(8888)
    # conn,add = socket.accept()
    tornado.ioloop.IOLoop.instance().start()
