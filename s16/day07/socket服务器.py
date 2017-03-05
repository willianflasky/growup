#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 8000))
phone.listen(5)
while True:
    conn, addr = phone.accept()
    print("TCP conn:", conn)
    print("cleint addr:", addr)
    while True:
        try:
            cmd = conn.recv(1024)
            if not cmd:        # 针对LINUX,CLIENT断开后,死循环
                break
            print("from client msg :{0}".format(cmd))
            res = subprocess.Popen(cmd.decode('utf8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                back_msg = err
            else:
                back_msg = res.stdout.read()
            conn.send(back_msg)
            print(back_msg)
        except Exception as e:
            break
    conn.close()
phone.close()


