#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import os
import sys
from shop import shop
from core import main


base_dir = os.path.normpath(os.path.join(os.path.abspath(__file__),
                                         os.pardir,
                                         ))
sys.path.insert(0, base_dir)

message = """\033[32;1m
<===================super market=================>
        请选择:
        1.ATM办理业务
        2.购物
        \033[0m
"""

print(message)


def run():
    while True:
        choice = input(">:").strip()
        if len(choice) == 0:
            continue
        if choice.isdigit():
            if int(choice) == 1:
                main.run()
            elif int(choice) == 2:
                shop.run()
            else:
                continue
        else:
            if choice == 'exit':
                exit()
            else:
                continue

if __name__ == '__main__':
    run()
