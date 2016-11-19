#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
import socket
ip_port=('127.0.0.1',9999)

#1.买手机
s=socket.socket()
#2.播号
s.connect(ip_port)
#3.发送消息
while True:
    send_data=input('>>:').strip()
    if send_data == 'exit':break
    if len(send_data) == 0:continue
    s.send(bytes(send_data,encoding='utf8'))
#4.收消息
    recv_data=s.recv(1024)
    print(str(recv_data,encoding='utf8'))
#5.挂电话
s.close()


