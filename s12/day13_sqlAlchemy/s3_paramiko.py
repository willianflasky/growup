#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


import paramiko
import uuid

class SSHConnection(object):
    def __init__(self,host='192.168.3.6',port=22,username='root',pwd='123456'):
        self.host=host
        self.port=port
        self.username=username
        self.pwd=pwd
        self.__k=None

    def connect(self):
        transport=paramiko.Transport((self.host,self.port))
        transport.connect(username=self.username,password=self.pwd)
        self.__transport=transport

    def close(self):
        self.__transport.close()

    def cmd(self,command):
        ssh = paramiko.SSHClient()
        ssh._transport = self.__transport

        stdin,stdout,stderr = ssh.exec_command(command)
        if stdout:
            result=stdout.read().decode()
        else:
            result=stderr.read().decode()
        return result

    def upload(self,local_path,target_path):
        sftp=paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(local_path,target_path)

    def download(self,target_path,local_path):
        sftp=paramiko.SFTPClient.from_transport(self.__transport)
        sftp.get(target_path,local_path)

ssh = SSHConnection()
ssh.connect()

r1=ssh.cmd('df -h')
print(r1)
#ssh.upload('s3_paramiko.py','/tmp/a.py')
#ssh.download('/tmp/a.py','tom.py')
ssh.close()