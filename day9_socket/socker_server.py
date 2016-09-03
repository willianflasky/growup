#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
import socket
ip_port=('127.0.0.1',9999)

#1.买手机
s=socket.socket()
#2.买手机卡
s.bind(ip_port)
#3.开机
s.listen(5)     #5最大挂起5个连接
#4.等待电话
while True:
    conn,addr=s.accept()
    #5.收消息
    while True:
            try:
                recv_data=conn.recv(1024) #1024字节
                if len(recv_data) == 0:break

                #print("----->",type(recv_data))
                #if str(recv_data,encoding='utf8') == 'exit':break
                #6.发消息
                send_data=recv_data.upper()
                conn.send(send_data)
            except Exception as e:
                break

    conn.close()

"""
回顾
1.基于python3.5版本socket只能收发字节,2.7可以收发字符串.
2.退出只在客户端退出就OK了.
3.s.accept()和recv是阻塞的.(基于连接正常是阻塞的)
4.listen(n)代表能挂起(等待)的连接数,如果n=1,代表可以连接 一个,等待一个,第三个拒绝报错.
5.服务端端口冲突,是因为没有释放,需要换端口.
6.客户端:1.send
        4.recv
  服务端:2.recv
        3.send
"""