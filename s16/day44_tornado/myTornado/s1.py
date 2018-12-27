#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/14 下午5:07
__author__ = "willian"

import tornado.ioloop
import tornado.web


# 解决登录认证的问题
class AuthHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.username = self.get_secure_cookie('userinfo')

    def prepare(self):
        pass


class HomeHandler(tornado.web.RequestHandler):
    # def get(self, nid):
    def get(self, *args, **kwargs):
        # print(nid)
        url = self.application.reverse_url('index')
        print(url)

        self.write('hello world!')


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html', msg="")

    def post(self):
        # GET
        # self.get_query_argument()
        # self.get_query_arguments()
        # # POST
        # self.get_body_argument()
        # self.get_body_arguments()
        #
        # # post and get
        # self.get_argument()
        # self.get_arguments()

        user = self.get_argument('user')
        pwd = self.get_argument('pwd')
        if user == 'alex' and pwd == "123":
            # self.set_cookie("userinfo", user)
            self.set_secure_cookie("userinfo", user)
            self.redirect("/index")
            return
        self.render("login.html", **{"msg": "用户名或者密码错误"})


class IndexHandler(AuthHandler):
    def get(self):
        if not self.username:
            self.redirect('/login')
            return
        user_list = ["willian", 'alex', 'tony']
        user_dict = {"id": '1', 'name': "alex"}
        self.render("index.html", user_list=user_list, user_dict=user_dict)


# 配置文件
settings = {
    'template_path': "templates",
    'static_path': "static",
    'static_url_prefix': "/static/",
    'xsrf_cookies': True,
    "cookie_secret": 'google',
}

application = tornado.web.Application([
    (r"/login", LoginHandler, {}, "login"),
    (r"/index", IndexHandler, {}, "index"),
    (r"/home/(\d+)", HomeHandler),
], **settings)

# 匹配域名后，优先在这里查询路由
# application.add_handlers("www.baidu.com", [
#     (r"/home/(\d+)", HomeHandler),
# ])

if __name__ == '__main__':
    # 实例化socket对象
    application.listen(8888)
    # conn,add = socket.accept()
    tornado.ioloop.IOLoop.instance().start()
