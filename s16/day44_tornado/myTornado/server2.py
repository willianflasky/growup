#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/30 下午3:12
__author__ = "willian"

import socket
import select


def f1(request):
    return "content 1"


def f2(request):
    return "content 2"


urls = [
    ('/index.html', f1),
    ('/home.html', f2),
]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 9999))
sock.listen(5)

input_list = [sock, ]

while True:
    rlist, wlist, elist = select.select(input_list, [], [], 0.005)

    for sk in rlist:
        # 新人来连接：sock
        if sk == sock:
            client, address = sock.accept()
            client.setsockopt(False)
            input_list.append(client)

        else:
            # 老人发来数据: client
            data = sk.recv(8096)
            response = f1(data)

            sk.sendall(response.encode('utf8'))
            sk.close()
