#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/30 下午6:05
__author__ = "willian"

import re
import socket
import select
import time


class HttpResponse(object):
    """
    封装响应信息
    """

    def __init__(self, content=''):
        self.content = content

        self.headers = {}
        self.cookies = {}

    def response(self):
        return bytes(self.content, encoding='utf-8')


class HttpNotFound(HttpResponse):
    """
    404时的错误提示
    """

    def __init__(self):
        super(HttpNotFound, self).__init__('404 Not Found')


class HttpRequest(object):
    """
    用户封装用户请求信息
    """

    def __init__(self, conn):
        self.conn = conn
        self.header_bytes = bytes()
        self.header_dict = {}
        self.body_bytes = bytes()

        self.method = ""
        self.url = ""
        self.protocol = ""

        self.initialize()
        self.initialize_headers()

    def initialize(self):

        header_flag = False
        while True:
            try:
                received = self.conn.recv(8096)
            except Exception as e:
                received = None
            if not received:
                break
            if header_flag:
                self.body_bytes += received
                continue
            temp = received.split(b'\r\n\r\n', 1)
            if len(temp) == 1:
                self.header_bytes += temp
            else:
                h, b = temp
                self.header_bytes += h
                self.body_bytes += b
                header_flag = True

    @property
    def header_str(self):
        return str(self.header_bytes, encoding='utf-8')

    def initialize_headers(self):
        headers = self.header_str.split('\r\n')
        first_line = headers[0].split(' ')
        if len(first_line) == 3:
            self.method, self.url, self.protocol = headers[0].split(' ')
            for line in headers:
                kv = line.split(':')
                if len(kv) == 2:
                    k, v = kv
                    self.header_dict[k] = v


class Future(object):
    """
    异步非阻塞模式时封装回调函数以及是否准备就绪
    """

    def __init__(self, callback):
        self.callback = callback
        self._ready = False
        self.value = None

    def set_result(self, value=None):
        self.value = value
        self._ready = True

    @property
    def ready(self):
        return self._ready


class TimeoutFuture(Future):
    """
    异步非阻塞超时
    """

    def __init__(self, timeout):
        super(TimeoutFuture, self).__init__(callback=None)
        self.timeout = timeout
        self.start_time = time.time()

    @property
    def ready(self):
        current_time = time.time()
        if current_time > self.start_time + self.timeout:
            self._ready = True
        return self._ready


class Snow(object):
    """
    微型Web框架类
    """

    def __init__(self, routes):
        self.routes = routes
        self.inputs = set()
        self.request = None
        self.async_request_handler = {}

    def run(self, host='localhost', port=9999):
        """
        事件循环
        :param host:
        :param port:
        :return:
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port,))
        sock.setblocking(False)
        sock.listen(128)
        sock.setblocking(0)
        self.inputs.add(sock)
        try:
            while True:
                readable_list, writeable_list, error_list = select.select(self.inputs, [], self.inputs, 0.005)
                for conn in readable_list:
                    # 新人来连接
                    if sock == conn:
                        client, address = conn.accept()
                        client.setblocking(False)
                        self.inputs.add(client)
                    # 老人传数据了
                    else:
                        gen = self.process(conn)
                        if isinstance(gen, HttpResponse):
                            conn.sendall(gen.response())
                            self.inputs.remove(conn)
                            conn.close()
                        else:
                            yielded = next(gen)
                            self.async_request_handler[conn] = yielded
                self.polling_callback()

        except Exception as e:
            pass
        finally:
            sock.close()

    def polling_callback(self):
        """
        遍历触发异步非阻塞的回调函数
        :return:
        """
        for conn in list(self.async_request_handler.keys()):
            yielded = self.async_request_handler[conn]
            if not yielded.ready:
                continue
            if yielded.callback:
                ret = yielded.callback(self.request, yielded)
                conn.sendall(ret.response())
            self.inputs.remove(conn)
            del self.async_request_handler[conn]
            conn.close()

    def process(self, conn):
        """
        处理路由系统以及执行函数
        :param conn:
        :return:
        """
        self.request = HttpRequest(conn)
        func = None
        for route in self.routes:
            if re.match(route[0], self.request.url):
                func = route[1]
                break
        if not func:
            return HttpNotFound()
        else:
            return func(self.request)

