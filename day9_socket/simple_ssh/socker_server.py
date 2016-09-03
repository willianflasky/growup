#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
import subprocess
import socket
ip_port=('127.0.0.1',9998)

#1.买手机
s=socket.socket()   #绑定协议,生成套接字
#2.买手机卡
s.bind(ip_port) #绑定IP + 端口 + 协议,用来唯一标识一个进程.ip port必须是元组格式.
#3.开机
s.listen(5)     #5最大挂起(等待)5个连接
#4.等待电话
while True: #用来重复接口新的连接.
    conn,addr=s.accept() #接受客户端的链接请求,返回conn相当于session,addr是客户端的IP地址和端口.
    #5.收消息
    while True: #用来基于一个链接重复收发消息.
            try:    #客户端可能异常关闭.
                recv_data=conn.recv(1024) #1024字节  收消息,阻塞
                if len(recv_data) == 0:break    #客户端如果退出,服务端将收到空消息,退出.

                #6.发消息
                p=subprocess.Popen(str(recv_data,encoding='utf8'),shell=True,stdout=subprocess.PIPE)    #执行系统命令
                res=p.stdout.read() #获取标准输出.
                if len(res) == 0:   #执行错误命令,标准输出为空.
                    send_data="cmd not found!"
                else:
                    send_data=str(res,encoding='utf-8') #执行OK,gbk-->str-->utf8

                #解决粘包
                ready_tag="Ready|%s"%len(send_data)
                conn.send(bytes(ready_tag,encoding='utf8'))
                feedback=conn.recv(1024)
                feedback=str(feedback,encoding='utf8')

                if feedback.startswith('Start'):
                    conn.send(bytes(send_data,encoding='utf8'))
            except Exception as e:
                break

    conn.close()

