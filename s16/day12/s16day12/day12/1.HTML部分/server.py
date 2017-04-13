#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


def handle_request(client):
    buf = client.recv(1024)

    client.send(b"HTTP/1.1 200 OK\r\n\r\n")
    f = open('a.html','rb')
    data = f.read()
    f.close()
    import time
    # data = data.replace(b'@@@name@@@',bytes(str(time.time()),encoding='utf-8'))
    client.send(data)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8003))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()