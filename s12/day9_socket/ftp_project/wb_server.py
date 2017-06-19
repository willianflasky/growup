#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import socketserver,json
import subprocess
import os

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(bytes('欢迎使用Myftp!',encoding='utf8'))

        while True:
            data=self.request.recv(1024)
            if len(data) == 0:break
            #print("[%s] says:%s"%(self.client_address,data.decode()))
            #self.request.sendall(bytes(data.upper()))

            str_data=data.decode()
            res=str_data.split('|')
            if  str_data.startswith('START'):
                ret=data.decode().split('|')
                f=open(ret[-1],'wb')
                FileSize=ret[1]
                FileSize=int(FileSize)
                counter=0
                self.request.sendall(bytes('ok',encoding='utf8'))

                while FileSize > counter:
                    temp_data=(self.request.recv(1024))
                    f.write(temp_data)
                    counter+=len(temp_data)

                self.request.send(bytes('Done',encoding='utf8'))
                f.close()
                print('---->DONE')
                continue

            elif res[0] == 'GET' or res[0] == 'get':
                file_name=res[1]
                if os.path.exists(file_name):
                    f=open(file_name,'rb')
                    file_size=os.stat(file_name).st_size
                    self.request.send(bytes('STARG|%s|%s'%(file_size,file_name),encoding='utf8'))

                    recv_data=self.request.recv(1024)
                    recv_data=recv_data.decode()
                    if recv_data== 'ok':
                        for line in f:
                            s.send(line)
                        recv_data=self.request.recv(1024)
                        recv_data=recv_data.decode
                        if recv_data =='Done':
                            print('%s transfer done!'%file_name)

                    else:
                        print(recv_data)

                else:
                    self.request.send(bytes('not found %s'%(file_name),encoding='utf8'))

            else:
                #ssh cmd
                p=subprocess.Popen(data,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
                ret=p.stdout.read()
                #print('---->',ret)
                if ret:
                    self.request.sendall(ret)   #subprocess输出为bytes,所以不需要bytes转换!
                else:
                    ret=p.stderr.read()
                    self.request.sendall(ret)



if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',9001),MyServer)
    server.serve_forever()