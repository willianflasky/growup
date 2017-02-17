#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import json
import os
import sys

current_user = {"username": None, 'login': False}


def get_json(args):
    base_dir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir))
    with open("{0}/db/accounts/{1}.json".format(base_dir, args), 'r') as f:
        data = json.load(f)
        return data


def login(func):
    def wrapper(*args, **kwargs):
        data = get_json(args[0])

        if current_user['username'] and current_user['login']:
            res = func(*args, **kwargs)
            return res

        password = input("password:").strip()

        if data['id'] == args[0] and data['password'] == password:
            current_user['id'] = args[0]
            current_user['login'] = True
            res = func(*args, **kwargs)
            return res
        else:
            print("用户或许密码错误!")
    return wrapper

if __name__ == '__main__':
    login()




