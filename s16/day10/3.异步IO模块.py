#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import select
import socket

sock = socket.socket()
inputs = [sock, ]


class Foo(object):
    def __init__(self):
        self.sock = socket.socket()

    def fileno(self):
        return self.sock.fileno()

r, w, e = select.select([sock, ], [], [], 1)
