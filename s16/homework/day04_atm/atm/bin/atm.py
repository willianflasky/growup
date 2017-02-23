#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import os
import sys

base_dir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, os.pardir,))
sys.path.insert(0, base_dir)

from atm.shop import shop
from atm.core import main
from atm.bin import manage


message = """\033[32;1m
[super market]
        请选择:
        1.ATM办理业务
        2.购物
        3.管理信用卡
        \033[0m
"""

print(message)

entry_menu = {
    1: main.run,
    2: shop.run,
    3: manage.run,
}


def run():
    while True:
        choice = input(">:").strip()
        if len(choice) == 0:
            continue
        if choice.isdigit():
            try:
                entry_menu[int(choice)]()
            except KeyError as e:
                print("not found!")
                continue
        else:
            if choice == 'exit':
                exit()
            else:
                continue

if __name__ == '__main__':
    run()

