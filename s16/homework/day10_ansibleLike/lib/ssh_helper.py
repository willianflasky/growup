#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import paramiko


class SshHelper(object):
    def __init__(self, host, port, username, pwd):
        self.host = host
        self.port = port
        self.username = username
        self.pwd = pwd
        self.transport = None

    def connect(self):
        transport = paramiko.Transport((self.host, self.port,))
        transport.connect(username=self.username, password=self.pwd)
        self.transport = transport

    def upload(self, local, target):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local, target)

    def cmd(self, cmd):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print("\n", stdout.read().decode('utf8'))

    def close(self):
        self.transport.close()


