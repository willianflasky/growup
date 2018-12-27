#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/30 下午3:12
__author__ = "willian"

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 9999))
sock.listen(5)
while True:
    client, address = sock.accept()
    data = client.recv(8096)

    # \r\n\r\n分割
    # 请求头中的URL
    # 请求体中数据
    # URL去路由头系中匹配（请求体中的数据）
    # response = func()

    client.sendall(b"xx")
    client.close()
