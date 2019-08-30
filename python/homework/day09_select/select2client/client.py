#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import socket
import json
import struct
import threading


def bar(client):
    data = client.recv(1024)
    return data


class Fn(object):
    @classmethod
    def put(cls, url):
        with open(url, 'rb') as f:
            return f.read()

    @classmethod
    def to_send(cls, dic, file):
        # 将字典-->json-->bytes
        head_bytes = json.dumps(dic).encode('utf8')
        # 发送头部长度
        client.send(struct.pack('i', len(head_bytes)))
        # 发送头部
        client.send(head_bytes)
        # 发送数据
        client.sendall(file)

client = socket.socket()
client.connect(('127.0.0.1', 8001))

while True:
    v = ""
    while True:
        inp = input(">>>>").strip()
        if inp == 'send':
            break
        if len(inp) == 0:
            continue
        v = inp + "\n" + v

    if v.startswith('put'):
        res = v.split()
        if len(res) == 1:
            print("\033[31;1mexample:\n put file.txt\033[0m")
            continue
        else:
            data = Fn.put(res[1])
            head_dic = {'cmd': 'put', 'file_name': res[-1], 'data_size': len(data)}
            Fn.to_send(head_dic, data)
    else:
        head_dic = {'cmd': 'chat', 'data_size': len(v)}
        Fn.to_send(head_dic, bytes(v, encoding='utf8'))

    ret = client.recv(1024)
    print("server respone:", ret)
client.close()
