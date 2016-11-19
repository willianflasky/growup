#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import socketserver,json
import subprocess

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(bytes('欢迎致电10086,请输入0转人工服务!',encoding='utf8'))

        while True:
            data=self.request.recv(1024)
            if len(data) == 0:break
            print("[%s] says:%s"%(self.client_address,data.decode()))

            task_data=json.loads(data.decode())
            task_action=task_data.get('action')
            if hasattr(self,"task_%s"%task_action):
                func=getattr(self,"task_%s"%task_action)
                func(task_data)
            else:
                print('task action is not supported',task_action)

    def task_put(self,*args,**kwargs):
        print("put",args,kwargs)
        file_size=args[0].get('file_size')
        file_name=args[0].get('file_name')
        f =open(file_name,'wb')
        recv_size=0
        while recv_size < file_size:
            data=self.request.recv(4096)
            f.write(data)
            recv_size +=len(data)
        print("file recv success.")
        f.close()

if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
    server.serve_forever()