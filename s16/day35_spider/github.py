#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import requests
from bs4 import BeautifulSoup
# 第一次请求: 获取 token and cookie
r1 = requests.get('https://github.com/login')
b1 = BeautifulSoup(r1.text, 'html.parser')
# get token
auth_token = b1.find(name='input', attrs={'name': 'authenticity_token'}).get('value')
# get cookies
r1_cookie_dict = r1.cookies.get_dict()


# 第二次请求: 发送用户认证
r2 = requests.post("https://github.com/session",
                   data={
                       'commit': "Sign in",
                       'utf8': '✓',
                       'authenticity_token': auth_token,
                       'login': '',
                       'password': ""
                   }, cookies=r1_cookie_dict)
# get cookies
r2_cookie_dict = r2.cookies.get_dict()

# 将两次的cookies合并
all_cookie_dict = {}
all_cookie_dict.update(r1_cookie_dict)
all_cookie_dict.update(r2_cookie_dict)


# 第三次请求:只有登录成功之后获取个人页面
r3 = requests.get('https://github.com/settings/emails', cookies=all_cookie_dict)
print(r3.text)


