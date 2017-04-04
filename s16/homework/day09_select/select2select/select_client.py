#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import socket
import json
import struct
import threading
import select

client = socket.socket()
client.connect(('127.0.0.1', 8001))

read_list = [client, ]
write_list = []
while True:
    v = ""
    while True:
        inp = input(">:").strip()
        if len(inp) == 0:
            continue
        if inp == 'exit':
            exit()
        if inp == 'send':
            write_list.append(client)
            break
        v = inp + "\n" + v

    r, w, e = select.select(read_list, write_list, [], 0.05)
    for obj in r:
        data = obj.recv(1024)
        if data:
            print(data)
            write_list.append(obj)
        else:
            print("关闭连接")
            obj.close()
            read_list.remove(obj)

    for obj in w:
        obj.sendall(bytes(v, encoding='utf8'))

client.close()




