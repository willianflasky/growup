#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
from atm.conf.settings import base_dir
import os
import json
import re


def check_new_id(n):
    curr_account_list = os.listdir("{0}/atm/db/accounts".format(base_dir))
    for file in curr_account_list:
        if int(file.split(".")[0]) == n:
            return True


def check_user(inp):
    while True:
        if inp.isdigit():
            inp = int(inp)
            if check_new_id(inp):
                print("{0}已经存在.".format(inp))
                break
            else:
                return True
        else:
            print("输入有误!")
            break


def check_date_format(inp):
    r = re.compile("([0-9]{4})-([0-9]{1,2})-([0-9]{1,2})")
    if r.match(inp):
        return True
    else:
        return False


def add_user():
    while True:
        card_id = input("card id:").strip()
        res = check_user(card_id)
        if res:
            break

    while True:
        card_pass = input("card pass:").strip()
        if len(card_pass) < 6:
            print("请输入6位以上.")
            continue
        else:
            break

    while True:
        card_balance = input("card balance:").strip()
        if card_balance.isdigit():
            card_balance = int(card_balance)
            break
        else:
            print("请输入数字!")
            continue

    while True:
        card_credit = input("card credit:").strip()
        if card_credit.isdigit():
            card_credit = int(card_credit)
            break
        else:
            print("请输入数字!")
            continue

    while True:
        card_status = input("card status:").strip()
        if card_status in ["0", "1", "2"]:
            break
        else:
            print("只有三种状态:0,1,2")
            continue

    while True:
        card_expire_date = input("card expire[2020-01-01]:").strip()
        res = check_date_format(card_expire_date)
        if res:
            break
        else:
            print("日期格式不对!")
            continue

    while True:
        card_enroll_date = input("card enroll[2011-01-01]:").strip()
        res = check_date_format(card_enroll_date)
        if res:
            break
        else:
            print("日期格式不对!")
            continue
    while True:
        card_pay_day = input("card pay_day:").strip()
        if card_pay_day.isdigit():
            card_pay_day = int(card_pay_day)
            break
        else:
            print("需要数字,1-31")
            continue

    new_user_dic = {
        "expire_date": card_expire_date,
        "pay_day": card_pay_day,
        "id": card_id,
        "enroll_date": card_enroll_date,
        "balance": card_balance,
        "password": card_pass,
        "status": card_status,
        "credit": card_credit,
    }

    with open("{0}/atm/db/accounts/{1}.json".format(base_dir, card_id), 'w') as f:
        json.dump(new_user_dic, f)
    print("done")


def change():
    card_id = input("card id:").strip()
    if card_id.isdigit():
        res = check_new_id(int(card_id))
        if res:
            with open("{0}/atm/db/accounts/{1}.json".format(base_dir, card_id), 'r') as f:
                data = json.load(f)
    while True:
        for k, v in data.items():
            print("\033[32;1m\t{0}:{1}\033[0m".format(k, v))
        column = input("修改字段:").strip()
        if len(column) == 0:
            continue
        elif column in data:
            new_value = input("修改成什么:").strip()
            if len(new_value) == 0:
                continue
            data[column] = new_value
            with open("{0}/atm/db/accounts/{1}.json".format(base_dir, card_id), 'w') as f:
                    json.dump(data, f)
            break

manage_menu = {
    1: add_user,
    2: change,
}


def run():
    admin_user = input("username:").strip()
    admin_pass = input("password:").strip()
    if admin_user == 'admin' and admin_pass == "admin":
        while True:
            print("1.add_user\n2.change")
            choice = int(input(">:").strip())
            if choice in manage_menu.keys():
                manage_menu[choice]()
            else:
                print("not found!")
    else:
        exit()


if __name__ == '__main__':
    run()
