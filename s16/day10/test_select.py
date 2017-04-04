#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import socket

server = socket.socket()
server.setblocking(False)
server.bind(("0.0.0.0", 8080))
server.listen(5)

inputs = [server]
outputs = []

while True:
    r, w, e = inputs, outputs, inputs
    if not (r or w or e): continue

    for obj in r:
        if obj is server:
            try:
                conn, addr = obj.accept()
            except BlockingIOError:
                pass
            else:
                conn.setblocking(False)
                inputs.append(conn)
        else:
            request = bytes()
            while True:
                try:
                    data = obj.recv(1024)
                except BlockingIOError:
                    data = None

                if not data: break

                request += data

            obj.sendall(request)

            obj.close()
            inputs.remove(obj)