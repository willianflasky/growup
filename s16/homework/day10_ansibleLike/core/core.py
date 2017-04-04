#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import threading
from core import verify
from core import display
from core import command


def run():
    res, user_dic = verify.verify()
    if res:
        res, result = display.display(user_dic)

        if res:
            while True:
                inp = input(">>>").strip()
                if len(inp) == 0: continue
                if inp == 'exit': exit()
                if hasattr(command.cmdHandler, inp):
                    func = getattr(command.cmdHandler, inp)
                    local = input("local_file>").strip()
                    target = input("target_file>").strip()
                    for line in result:
                        t = threading.Thread(target=func, args=(line, local, target))
                        t.start()
                else:
                    for line in result:
                        t = threading.Thread(target=command.worker, args=(line, inp,))
                        t.start()
        else:
            print("\033[32;1m没有主机.\033[0m")
            exit()
    else:
        exit()


