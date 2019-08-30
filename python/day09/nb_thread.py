#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

from concurrent.futures import ThreadPoolExecutor

import requests


def download(url):
    response = requests.get(url)
    return response


def run(url_list):
    pool = ThreadPoolExecutor(2)
    for item in url_list:
        url = item['url']
        call = item['call']
        future = pool.submit(download, url)
        future.add_done_callback(call)

