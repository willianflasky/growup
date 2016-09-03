#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
import socket
ip_port=('127.0.0.1',9998)

#1.买手机
s=socket.socket()
#2.播号
s.connect(ip_port)
#3.发送消息
while True: #基于connect建立的连接来循化发消息
    send_data=input('>>:').strip()
    if send_data == 'exit':break
    if len(send_data) == 0:continue
    s.send(bytes(send_data,encoding='utf8'))

    #4.收消息  解决粘包问题  #recv
    ready_tag=s.recv(1024)
    ready_tag=str(ready_tag,encoding='utf8')
    if ready_tag.startswith('Ready'):
        msg_size=int(ready_tag.split('|')[1])  #获取size
                #send
    start_tag='Start'
    s.send(bytes(start_tag,encoding='utf8'))

    #基于已经收到的待接收数据长度,循化接收数据.
    recv_size=0
    recv_msg=b''
    while recv_size < msg_size:
        recv_data=s.recv(1024)
        recv_msg +=recv_data
        recv_size +=len(recv_data)
        print("MSG SIZE %s RECV SIZE %s"%(msg_size,recv_size))
    print(str(recv_msg,encoding='utf8'))

#5.挂电话
s.close()


