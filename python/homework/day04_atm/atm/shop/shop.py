#!/usr/bin/env python
# coding:utf8
__author__ = "willian"

from atm.core.main import consume
from atm.core.main import user_data
from atm.core.logger import logger
from atm.core import auth


trans_logger = logger('transaction')
access_logger = logger('access')


def run():
    # dictionary
    shop_list = [
        ['iphone', 6500],
        ['mac', 12000],
        ['office', 30],
        ['bag', 200],
        ['watch', 2000],
    ]

    welcome_message = """\033[31;0m
        欢迎来购物,祝您购物愉快!
        \033[0m
    """

    print(welcome_message)

    car = []
    total = 0

    # print list
    for k, v in enumerate(shop_list, 1):
        print(k, v[0], v[1])

    while True:
        choice = input("你想买点什么?")
        if choice.isalpha():
            if choice == 'exit' or 'quit':
                for i in car:
                    print("你购买了:\033[32;1m{0},{1}\033[0m".format(i[0], i[1]))
                    total += i[1]
                print("total:\033[31;1m{0}\033[0m".format(total))
                # flush car:
                acc_data = auth.acc_login(user_data, access_logger)
                user_data['account_data'] = acc_data
                if user_data["is_authenticated"]:
                    res = consume(user_data, total)
                    if res == 'fail':
                        print("信用卡额度不够!")
                    elif res:
                        print("欢迎再来!")
                        exit()
            else:
                continue

        elif choice.isdigit:
            choice = int(choice)
            if choice <= len(shop_list):
                ret = shop_list[choice-1]
                car.append(ret)
            else:
                print("\033[31;1m没有些商品.\033[0m")
                continue

if __name__ == '__main__':
    run()





