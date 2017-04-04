#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import socket
import select


# 中间封装一层
class Foo(object):
    def __init__(self, sock, callback, url, host):
        self.sock = sock
        self.callback = callback
        self.url = url
        self.host = host

    def fileno(self):
        return self.sock.fileno()


class NbIO(object):
    def __init__(self):
        self.fds = []
        self.connections = []

    def connect(self, url_list):
        for item in url_list:
            conn = socket.socket()
            conn.setblocking(False)
            # 1. 发送链接请求
            try:
                conn.connect((item['host'], 80))
            except BlockingIOError as e:
                pass
            obj = Foo(conn, item['callback'], item['url'], item['host'])
            self.fds.append(obj)
            self.connections.append(obj)

    def send(self):
        while True:
            if len(self.fds) == 0:
                break
            # wList，有对象；当前socket已经创建链接
            rList, wList, eList = select.select(self.fds, self.connections, self.fds, 0.5)

            for obj in rList:
                # 4.有数据响应回来了
                conn = obj.sock
                data = bytes()
                while True:
                    try:
                        d = conn.recv(1024)
                        data = data + d
                    except BlockingIOError as e:
                        d = None
                    if not d:
                        break
                # print(data)
                obj.callback(data)  # 自定义操作 f1  f2
                self.fds.remove(obj)
                # print(len(self.fds),len(self.connections))
                # 执行当前请求 函数：f1  f2
            # 【1,2,3，】
            for obj in wList:
                # 2.已经连接上远程
                conn = obj.sock
                # 3. 发送数据
                # HTTP/1.1\r\nHost: %s\r\n\r\n
                template = "GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (obj.url, obj.host,)
                # template = "POST %s HTTP/1.1\r\nHost: 127.0.0.1:8888\r\n\r\nk1=v1&k2=v2" %(obj.url,)
                conn.sendall(template.encode('utf-8'))
                self.connections.remove(obj)
