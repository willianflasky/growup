#!/usr/bin/python
# -*- coding:utf-8 -*-
# import requests
# #
# # r1 = requests.get('http://127.0.0.1:8000/login/')
# #
# # r2 = requests.post(
# #     url='http://127.0.0.1:8000/login/',
# #       data={
# #           'csrfmiddlewaretoken': "31tFZX2IZ0blOTfZ5VmfXDMLuvYaTaSjajVCiAWje07nuPLRJa6DvsXIRyzczXBh",
# #           'username': 'alex',
# #           'password': '123',
# #           'code': "sidfjsd"
# #
# #       }
# # )
# # print(r2.text)
#
#
# ### 1、首先登陆任何页面，获取cookie
#
# i1 = requests.get(url="http://dig.chouti.com/help/service")
#
# ### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
# i2 = requests.post(
#     url="http://dig.chouti.com/login",
#     data={
#         'phone': "8615131255089",
#         'password': "woshiniba",
#         'oneMonth': ""
#     },
#     cookies=i1.cookies.get_dict()
# )
#
# ### 3、点赞（只需要携带已经被授权的gpsd即可）
# gpsd = i1.cookies.get_dict()['gpsd']
# i3 = requests.post(
#     url="http://dig.chouti.com/link/vote?linksId=12439696",
#     cookies={'gpsd': gpsd}
# )
# print(i3.text)


# v = [
#     {'id': 1,'name': 'alex'},
#     {'id': 1,'name': 'alex'},
#     {'id': 1,'name': 'alex'},
# ]
# for row in v:
#     row['email'] = '234'
# print(v)

# 字典和列表
# v1 = [1,2,3,4]
# v2 = v1
# v1.append(123123)
# print(v2)

# v1 = 123123
# v2 = v1
# v1 = 666
# print(v2)

# v1 = [1,2,3,4]
# v2 = v1
# v1 = ['a','b']
# print(v2)


# v1 = [
#     {'id':1 ,'child': [内存地址]},
#     {'id':2 ,'child': []},
# ]
# v1[0]['child'].append(v1[1])
# v1[1]['email'] = "sdfsdf"
# print(v1)


comment_list = [
    {'id': 1, 'news_id': 1, 'user_id': 10, 'content': "写的什么玩意呀", 'reply_id': None},
    {'id': 2, 'news_id': 1, 'user_id': 11, 'content': "还真不是玩意 ", 'reply_id': 1},
    {'id': 3, 'news_id': 1, 'user_id': 12, 'content': "写的真好 ", 'reply_id': 1},
    {'id': 4, 'news_id': 1, 'user_id': 11, 'content': "写的真好 ", 'reply_id': 3},
    {'id': 5, 'news_id': 1, 'user_id': 19, 'content': "sdfsfsdsd ", 'reply_id': None},
]

comment_dict = {}
for row in comment_list:
    row['child'] = []
    comment_dict[row['id']] = row

for row in comment_list:
    if row['reply_id']:
        reply_id = row['reply_id']
        comment_dict[reply_id]['child'].append(row)

commen_reuslt = {}
for k,v in comment_dict.items():
    if v['reply_id'] == None:
        commen_reuslt[k] = v

