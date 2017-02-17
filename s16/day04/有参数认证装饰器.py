#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

user_list = [
    {'name': 'alex', 'passwd': '123'},
    {'name': 'linhaifeng', 'passwd': '123'},
]

current_user = {'username':None,'login':False}


def auth(auth_type='file'):
    def inner(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'file':
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
            elif auth_type == 'ldap':
                print("from ldap auth!")
                res = func(*args, **kwargs)
                return res
        return wrapper
    return inner

"""
#auth(auth_type='file')就是在运行一个函数,然后返回inner,所以@auth(auth_type='file')
#就相当于@inner,只不过现在,我们的inner作为一个闭包的应用,
#外层的包auth给它留了一个auth_type='file'参数
"""


@auth(auth_type='file')
def index():
    print('欢迎来到主页面')


@auth(auth_type='ldap')
def home():
    print('这里是你家')


index()
home()



