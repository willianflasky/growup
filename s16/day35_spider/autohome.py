#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import requests
from bs4 import BeautifulSoup

# response = requests.get("http://www.autohome.com.cn/news/")
# # response.text 是str
# # response.content 是bytes二进制
#
# response.encoding = 'gbk'   # 网站使用了gbk
# root = BeautifulSoup(response.text, 'html.parser')   # 将返回结果拿到用bs解析
# outer_div_obj = root.find(name='div', id='auto-channel-lazyload-article')  # 打到div id='xx'
# li_obj_list = outer_div_obj.find_all(name='li')     # 拿到里面所有的LI
#
# for li_obj in li_obj_list:
#     if not li_obj.find('h3'):
#         continue
#     title_obj = li_obj.find('h3')       # 拿到对象 H3标签
#     summary_obj = li_obj.find('p')      # 拿到对象 P标签
#     img_obj = li_obj.find('img')        # 拿到对象 IMG标签
#     src = img_obj.attrs.get('src')      # 从IMG标签对象中拿到src属性
#
#     print(src, title_obj.text, summary_obj.text)

response = requests.get("http://www.autohome.com.cn/news/")
response.encoding = 'gbk'

soup = BeautifulSoup(response.text, 'html.parser')
tag = soup.find(name='div', attrs={'id': 'auto-channel-lazyload-article'})
li_list = tag.find_all('li')

for li in li_list:
    h3 = li.find('h3')

    if not h3:
        continue
    print("\033[33;1m标题: {0}\033[0m".format(h3.text))
    print("\033[34;1m路径: http://{0}\033[0m".format(li.find('img').attrs['src']))
    print("\033[34;1m内容: {0}\033[0m".format(li.find('p').text))


