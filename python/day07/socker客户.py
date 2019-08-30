#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8000))
while True:
    cmd = input(">>:").strip()
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))
    res = client.recv(1024)
    print(res.decode('utf8'))
client.close()
