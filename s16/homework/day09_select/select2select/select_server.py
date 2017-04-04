#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import select
import socket


sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk1.bind(('127.0.0.1', 8001),)
sk1.listen(5)

sk2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk2.bind(('127.0.0.1', 8002),)
sk2.listen(5)

inputs = [sk1, sk2]
write_list = []
while True:
    r, w, e = select.select(inputs, write_list, [], 0.05)

    for obj in r:
        if obj in [sk1, sk2]:
            print("新连接....")
            conn, addr = obj.accept()
            inputs.append(conn)
        else:               # 连接发数据过来
            print("有用户发数据了...")
            # 收头长度
            data = obj.recv(1024)
            if data:
                print(str(data, encoding='utf8'))
                write_list.append(obj)
            else:           # 没有数据
                print("close done")
                obj.close()
                inputs.remove(obj)

    for obj in write_list:
        v = ""
        while True:
            inp = input("server> ").strip()
            if inp == 'send':
                break
            elif len(inp) == 0:
                continue
            v = inp + "\n" + v
        obj.sendall(bytes(v, encoding='utf8'))



