#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


import socket
import os,json

ip_port=('127.0.0.1',9001)
s=socket.socket()
s.connect(ip_port)
welcome_msg=s.recv(1024)
print('from server:',welcome_msg.decode())

while True:
    send_data=input('>>:').strip()
    if len(send_data) == 0: continue

    #put
    ret=send_data.split(' ')
    if ret[0] == 'put':
        f=open(ret[1],'rb')
        FileSize=os.stat(ret[1]).st_size
        FileName=ret[1].split('/')[-1]

        #send size,start and fname
        StartInfo="START|%s|%s"%(FileSize,FileName)
        s.send(bytes(StartInfo,encoding='utf8'))
        #recv ok
        recv_data = s.recv(1024)
        print('---->ok',recv_data)
        if recv_data.decode() == 'ok':
            for line in f:
                s.send(line)
            recv_data=s.recv(1024)
            if recv_data.decode() == 'Done':
                print(recv_data.decode())
                continue

    elif ret[0] == 'get':
        FileName=ret[1]
        s.sendall(bytes('GET|%s'%FileName,encoding='utf8'))
        recv_data = s.recv(1024)
        recv_data=recv_data.decode()
        status=recv_data.split('|')

        if status[0] == 'START':
            s.sendall(bytes('ok',encoding='utf8'))
            file_size=status[1]
            file_size=int(status[1])
            file_name=status[-1]
            counter=0
            f=open(file_name,'wb')
            while file_size > counter:
                temp_data=s.recv(1024)
                f.write(temp_data)
                counter +=len(temp_data)
            s.send(bytes('Done',encoding='utf8'))
            f.close()

        else:
            print(recv_data)
    else:
        s.send(bytes(send_data,encoding='utf8'))
        recv_data=s.recv(1024)
        print(recv_data.decode())

s.close()
