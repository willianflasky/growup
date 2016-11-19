#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
import paramiko
import sys
import os
import socket
import select
import getpass
import termios
import tty
from paramiko.py3compat import u

tran = paramiko.Transport(('192.168.3.6', 22,))
tran.start_client()
tran.auth_password('willian', '100200')

# 打开一个通道
chan = tran.open_session()
# 获取一个终端
chan.get_pty()
# 激活器
chan.invoke_shell()


# 获取原tty属性
oldtty = termios.tcgetattr(sys.stdin)
try:
    # 为tty设置新属性
    # 默认当前tty设备属性：
    #   输入一行回车，执行
    #   CTRL+C 进程退出，遇到特殊字符，特殊处理。

    # 这是为原始模式，不认识所有特殊符号
    # 放置特殊字符应用在当前终端，如此设置，将所有的用户输入均发送到远程服务器
    tty.setraw(sys.stdin.fileno())
    chan.settimeout(0.0)

    while True:
        # 监视 用户输入 和 远程服务器返回数据（socket）
        # 阻塞，直到句柄可读
        r, w, e = select.select([chan, sys.stdin], [], [], 1)
        if chan in r:
            try:
                x = u(chan.recv(1024))
                if len(x) == 0:
                    print('\r\n*** EOF\r\n')
                    break
                sys.stdout.write(x)
                sys.stdout.flush()
            except socket.timeout:
                pass
        if sys.stdin in r:
            x = sys.stdin.read(1)
            if len(x) == 0:
                break
            chan.send(x)

finally:
    # 重新设置终端属性
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

chan.close()
tran.close()