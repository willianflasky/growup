#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from concurrent.futures import ThreadPoolExecutor
import requests


def txt(future):
    download_response = future.result()     # future.result()就是把response取出来
    print("处理中,,", download_response.url, download_response.status_code)


def task(url):
    response = requests.get(url)
    return response

url_list = [
    'http://www.baidu.com',
    'http://www.sina.com.cn',
    'http://www.autohome.com.cn'
    ]

pool = ThreadPoolExecutor(2)

for url in url_list:
    future = pool.submit(task, url)  # future中包括response,当然还有其它
    future.add_done_callback(txt)
