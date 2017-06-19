#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import paramiko

#basic
"""
#private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
#ssh.connect(hostname='192.168.3.6', port=22, username='root', key=private_key)
ssh.connect(hostname='192.168.3.6', port=22, username='root', password='123456')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ls /')
# 获取命令结果
result = stdout.read()
# 关闭连接
ssh.close()

"""

"""
#transport
class ssh(object):
    def __init__(self,ip,port,username,password):
        self.ip=ip
        self.port=port
        self.username=username
        self.password=password

    def run(self,cmd):
        transport = paramiko.Transport((self.ip,self.port))
        transport.connect(username=self.username, password=self.password)

        ssh = paramiko.SSHClient()
        ssh._transport = transport

        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
        transport.close()


ssh=ssh('192.168.3.6',22,'root','123456')
ssh.run('df -h')
"""


#transport key
class ssh(object):
    def __init__(self,ip,port,username,key):
        self.ip=ip
        self.port=port
        self.username=username
        self.key=key

    def run(self,cmd):
        transport = paramiko.Transport((self.ip,self.port))
        transport.connect(username=self.username,pkey=paramiko.RSAKey.from_private_key_file(self.key))

        ssh = paramiko.SSHClient()
        ssh._transport = transport

        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
        transport.close()

ssh=ssh('192.168.3.6',22,'root','/root/.ssh/id_rsa')
ssh.run('df -h')

