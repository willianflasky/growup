#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from concurrent.futures import ThreadPoolExecutor
import requests


def task(url):
    response = requests.get(url)
    print("得到结果:", url, len(response.content))

url_list = [
    'http://www.baidu.com',
    'http://www.sina.com.cn',
    'http://www.autohome.com.cn'
    ]

pool = ThreadPoolExecutor(2)

for url in url_list:
    print("请求开始", url)
    pool.submit(task, url)
