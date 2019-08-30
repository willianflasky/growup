#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/4/2 上午11:58
__author__ = "willian"

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 8002))
sock.listen(5)
# 获取客户端socket对象
conn, address = sock.accept()
# 获取客户端的【握手】信息
data = conn.recv(1024)
print(data)
conn.send('响应【握手】信息')
conn.close()
