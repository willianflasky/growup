#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import os
import sys
import json
from core import auth

base_dir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir))


@auth.login
def account_info(car_id):
    data = auth.get_json(car_id)
    for k, v in data.items():
        print("\033[33;0m{0}:{1}\033[0m".format(k, v))


def repay(car_id):
    pass


def withdraw(car_id):
    pass


def transfer(car_id):
    pass


def pay_check(car_id):
    pass


def logout(car_id):
    pass

menu = """
 ------- Oldboy Bank ---------
    \033[32;1m1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    6.  退出
    \033[0m
    """

menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }


def run():
    while True:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            car_id = input("car ID:").strip()
            menu_dic[user_option](int(car_id))


if __name__ == '__main__':
    run()
