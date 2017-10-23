#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import requests
from bs4 import BeautifulSoup

# 1. 请求获取cookies
r0 = requests.get("http://dig.chouti.com")
r0_cookie_dict = r0.cookies.get_dict()


# 2. 授权
r1 = requests.post(
    url="http://dig.chouti.com/login",
    data={
        'phone': 'xx',
        'password': 'xx',
        'oneMonth': 1
    },
    cookies=r0_cookie_dict
)
r1_cookie_dict = r1.cookies.get_dict()

all_cookies = {}
all_cookies.update(r0_cookie_dict)
all_cookies.update(r1_cookie_dict)

# 3.点赞
r2 = requests.post(url='http://dig.chouti.com/link/vote?linksId=14808951', cookies=all_cookies)
print(r2.text)


