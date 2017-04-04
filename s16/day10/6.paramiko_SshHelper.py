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

    def put(self, local, target):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        # 将location.py 上传至服务器 /tmp/test.py
        sftp.put(local, target)

    def get(self, remote, local):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.get(remote, local)

    def cmd(self, cmd):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(cmd)
        stdout.read()

    def close(self):
        self.transport.close()

if __name__ == '__main__':
    obj = SshHelper('1.1.1.1')
    obj.connect()
    obj.close()
