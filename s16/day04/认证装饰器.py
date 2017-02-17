#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

user_list = [
    {'name': 'alex', 'passwd': '123'},
    {'name': 'linhaifeng', 'passwd': '123'},
]

current_user = {'username':None,'login':False}



def auth(func):
    def wrapper(*args, **kwargs):
        if current_user['username'] and current_user['login']:
            res = func(*args, **kwargs)
            return res

        username = input("username>").strip()
        password = input("password>").strip()

        for number, value in enumerate(user_list):
            if value['name'] == username and value['passwd'] == password:
                current_user['username'] = username
                current_user['login'] = True
                res = func(*args, **kwargs)
                return res
                break
            else:
                print("用户或许密码错误!")
    return wrapper


@auth
def index():
    print('欢迎来到主页面')


@auth
def home():
    print('这里是你家')


index()
home()



