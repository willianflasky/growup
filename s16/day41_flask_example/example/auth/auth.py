#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import request, session,redirect


# 登录成功时 _request_ctx_stack.top.user = user


class Auth(object):
    def __init__(self, app=None):
        self.app = app
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.auth_manager = self

        app.before_request(self.check_login)
        app.context_processor(self.auth_context_processor)

    def auth_context_processor(self):
        name = session.get('user')
        return dict(current_user=name)

    def check_login(self):
        # print(request.url)
        # print(request.path)
        if request.path == '/login':
            return None

        if session.get('user'):
            return None
        return redirect('/login')

    def permission(self):
        pass

    def login(self,data):
        session['user'] = data