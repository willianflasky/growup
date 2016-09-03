#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


import socket
import os,json

ip_port=('127.0.0.1',9000)
s=socket.socket()
s.connect(ip_port)
welcome_msg=s.recv(1024)
print('from server:',welcome_msg.decode())

while True:
    send_data=input('>>:').strip()
    if len(send_data) == 0: continue
    cmd_list = send_data.split()
    if len(cmd_list) < 2:continue
    task_type=cmd_list[0]
    if task_type == 'put':
        abs_filepath=cmd_list[1]
        if os.path.isfile(abs_filepath):
            file_size=os.stat(abs_filepath).st_size
            filename=abs_filepath.split('/')[-1]
            print('file:%s size:%s' %(abs_filepath,file_size))
            msg_data={'action':'put','filename':filename,'file_size':file_size}
            s.send(bytes(json.dumps(msg_data),encoding='utf8'))

            print("start sending file",filename)
            f = open(abs_filepath,'rb')
            for line in f:
                s.send(line)
            print("send file done")
        else:
            print("\033[31;1mfile [%s] is not exist\033[0m"%abs_filepath)
            continue
    else:
        print('doesn\'t suport task type',task_type)
        continue


    #s.send(bytes(send_data,encoding='utf8'))

    recv_data=s.recv(1024)
    print(recv_data.decode())

s.close()
