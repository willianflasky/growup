#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import socketserver
import os
import sys
import subprocess
import struct
import json

BASE_DIR = os.path.normpath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.insert(0, BASE_DIR)

from conf import settings
from lib import active


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):       # handle里只写通讯循环
        print("服务端启动...")
        while True:
            conn = self.request
            print(self.client_address)
            while True:
                head_dict_len = conn.recv(4)
                if head_dict_len:
                    head_dict = json.loads(conn.recv(struct.unpack('i', head_dict_len)[0]).decode('utf8'))

                    if head_dict['cmd'] == 'put' and len(head_dict) != 1:
                        active.put(conn, **head_dict)
                    elif head_dict['cmd'] == 'get' and len(head_dict) != 1:
                        active.get(conn, **head_dict)

                    else:   # 处理命令
                        res = subprocess.Popen(head_dict['cmd'], shell=True,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                        err = res.stderr.read()
                        if err:
                            client_data = err
                        else:
                            client_data = res.stdout.read()

                        # 发送数据---->
                        # 第一, 制作头部
                        headers = {'data_size': len(client_data), }
                        headers_bytes = json.dumps(headers).encode('utf8')
                        # 第二, 发送报头长度
                        conn.send(struct.pack('i', len(headers_bytes)))
                        # 第三, 发送报头
                        conn.send(headers_bytes)
                        # 第四, 发送数据
                        conn.sendall(client_data)
            conn.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer((settings.HOST, settings.PORT), MyServer)
    server.serve_forever()  # 处理连接循环
