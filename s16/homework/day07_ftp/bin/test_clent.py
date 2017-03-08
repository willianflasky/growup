#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"


import socket
import struct
import json

ip_port = ('127.0.0.1', 4000)
sk = socket.socket()
sk.connect(ip_port)
print("客户端启动：")
while True:
    inp = input('>>>')
    if len(inp) == 0:
        continue       # 按回车,发送数据为空时卡住.
    elif inp == 'exit':
        break
    sk.sendall(bytes(inp, "utf8"))

    # 收到头部长度
    header = sk.recv(4)
    head_size = struct.unpack('i', header)[0]
    # 收头部
    head_bytes = sk.recv(head_size)
    head_json = head_bytes.decode('utf8')
    headers = json.loads(head_json)

    # 获取真实数据长度
    data_size = headers['data_size']

    # 收取真实数据
    recv_size = 0
    recv_bytes = b''
    while recv_size < data_size:
        ret = sk.recv(1024)
        recv_bytes += ret
        recv_size += len(ret)

    print(str(recv_bytes, "utf8"))
sk.close()
