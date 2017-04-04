#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import socket

client = socket.socket()

client.connect(('127.0.0.1', 8001))

while True:
    v = input(">>>>")
    if v == 'exit':
        break
    client.sendall(bytes(v, encoding='utf8'))
    ret = client.recv(1024)
    print("server respone:", ret)

client.close()
