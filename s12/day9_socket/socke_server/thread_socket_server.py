#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import socketserver
import subprocess

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(bytes('欢迎致电10086,请输入0转人工服务!',encoding='utf8'))

        while True:
            data=self.request.recv(1024)
            if len(data) == 0:break
            print("[%s] says:%s"%(self.client_address,data.decode()))
            #self.request.sendall(data.upper())

            cmd=subprocess.Popen(data.decode(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            cmd_res=cmd.stdout.read()   #subprocess's output is bytes.
            if not cmd_res:
                cmd_res = cmd.stderr.read()
            if len(cmd_res) == 0:  #when cmd has not output
                cmd_res=bytes('cmd has not output.',encoding='utf8')
            self.request.sendall(cmd_res)
if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
    server.serve_forever()