#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import select
import socket


class Flask(object):
    def __init__(self, routers):
        self.routers = routers

    def process_data(self, client):
        data = bytes()
        while True:         # 接收数据循环
            try:
                trunk = client.recv(1024)  # 没有数据会报错, 用户断开也会报错.
            except BlockingIOError as e:
                trunk = ""
            if not trunk:
                break
            data += trunk

        data_str = str(data, encoding='utf8')
        header, body = data_str.split('\r\n\r\n', 1)
        header_list = header.split('\r\n')
        header_dict = {}
        for line in header_list:
            value = line.split(":", 1)
            if len(value) == 2:
                k, v = value
                header_dict[k] = v
            else:
                header_dict['mothod'], header_dict['url'], header_dict['protocol'] = line.split(' ')

        return header_dict, body

    def run(self, host='127.0.0.1', port=8888):
        sock = socket.socket()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setblocking(False)
        sock.bind((host, port))
        sock.listen(5)

        inputs = [sock, ]
        while True:
            rList, wList, eList = select.select(inputs, [], [], 0.5)
            for client in rList:
                # 建立新的连接
                if client == sock:
                    conn, addr = client.accept()
                    conn.setblocking(False)
                    inputs.append(conn)
                else:           # 用户发送数据
                    header_dict, body = self.process_data(client)
                    request_url = header_dict['url']
                    func_name = None
                    for item in self.routers:
                        if item[0] == request_url:
                            func_name = item[1]
                            break
                    if not func_name:
                        client.sendall(b"404")
                    else:
                        result = func_name(header_dict, body)
                        client.sendall(result.encode('utf8'))
                    inputs.remove(client)
                    client.close()

