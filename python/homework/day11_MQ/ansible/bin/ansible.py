#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import os
import sys
import uuid
import threading

BASE_DIR = os.path.normpath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.insert(0, BASE_DIR)

from lib import recv
from lib import send


def recv_back(my_uuid):
    r1 = recv.recver()
    r1.exchange(my_uuid)
    r1.run()
    r1.close()


if __name__ == '__main__':
    s1 = send.sender()
    while True:
        cmd = input(">>>").strip()
        if len(cmd) == 0:
            continue
        if cmd == 'exit':
            exit()
        my_uuid = str(uuid.uuid4())
        s1.run('webserver', cmd, my_uuid)
        t = threading.Thread(target=recv_back, args=(my_uuid, ))
        t.start()


