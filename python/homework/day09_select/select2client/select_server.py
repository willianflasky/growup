#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import select
import socket
import struct
import json
import os


class Fns(object):
    @classmethod
    def save(cls, filename, data):
        with open(filename, 'wb') as f:
            f.write(data)

sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk1.bind(('127.0.0.1', 8001),)
sk1.listen(5)

sk2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sk2.bind(('127.0.0.1', 8002),)
sk2.listen(5)

inputs = [sk1, sk2]
while True:
    r, w, e = select.select(inputs, [], [], 0.05)

    for obj in r:
        if obj in [sk1, sk2]:
            print("新连接....")
            conn, addr = obj.accept()
            inputs.append(conn)
        else:               # 连接发数据过来
            print("有用户发数据了...")
            # 收头长度
            header = obj.recv(4)
            if header:
                head_size = struct.unpack('i', header)[0]
                # 收头部
                headers = json.loads(obj.recv(head_size).decode('utf8'))
                # 获取真实数据长度
                data_size = headers['data_size']
                # 收取真实数据
                recv_size = 0
                recv_bytes = b''
                while recv_size < data_size:
                    ret = obj.recv(1024)
                    recv_bytes += ret
                    recv_size += len(ret)
                if headers['cmd'] == 'put':
                    file_name = os.path.basename(headers['file_name'])
                    Fns.save(file_name, recv_bytes)
                    obj.send(bytes('transfer done.', encoding='utf8'))
                elif headers['cmd'] == 'chat':
                    v = ""
                    print(recv_bytes.decode('utf8'))
                    while True:
                        inp = input("server> ").strip()
                        if inp == 'send':
                            break
                        elif len(inp) == 0:
                            continue
                        v = inp + "\n" + v

                    obj.sendall(bytes(v, encoding='utf8'))

            else:           # 没有数据
                print("close done")
                obj.close()
                inputs.remove(obj)

