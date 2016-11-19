#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import paramiko

transport = paramiko.Transport(('192.168.3.6',22))
transport.connect(username='root',password='123456')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('14_paramiko.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('/tmp/test.py', 'test.py')

transport.close()


"""

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')

transport = paramiko.Transport(('hostname', 22))
transport.connect(username='wupeiqi', pkey=private_key )

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('remove_path', 'local_path')

transport.close()


"""