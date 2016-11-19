#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import paramiko
import sys
import os
import socket
import getpass

from paramiko.py3compat import u

# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan):
    if has_termios:
        posix_shell(chan)
    else:
        windows_shell(chan)


def posix_shell(chan):
    import select

    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        log = open('handle.log', 'a+', encoding='utf-8')
        flag = False
        temp_list = []
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break
                    if flag:
                        if x.startswith('\r\n'):
                            pass
                        else:
                            temp_list.append(x)
                        flag = False
                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)
                import json

                if len(x) == 0:
                    break

                if x == '\t':
                    flag = True
                else:
                    temp_list.append(x)
                if x == '\r':
                    log.write(''.join(temp_list))
                    log.flush()
                    temp_list.clear()
                chan.send(x)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)


def windows_shell(chan):
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")

    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(data)
            sys.stdout.flush()

    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()

    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass


def run():
    default_username = getpass.getuser()
    username = input('Username [%s]: ' % default_username)
    if len(username) == 0:
        username = default_username


    hostname = input('Hostname: ')
    if len(hostname) == 0:
        print('*** Hostname required.')
        sys.exit(1)

    tran = paramiko.Transport((hostname, 22,))
    tran.start_client()

    default_auth = "p"
    auth = input('Auth by (p)assword or (r)sa key[%s] ' % default_auth)
    if len(auth) == 0:
        auth = default_auth

    if auth == 'r':
        default_path = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
        path = input('RSA key [%s]: ' % default_path)
        if len(path) == 0:
            path = default_path
        try:
            key = paramiko.RSAKey.from_private_key_file(path)
        except paramiko.PasswordRequiredException:
            password = getpass.getpass('RSA key password: ')
            key = paramiko.RSAKey.from_private_key_file(path, password)
        tran.auth_publickey(username, key)
    else:
        pw = getpass.getpass('Password for %s@%s: ' % (username, hostname))
        tran.auth_password(username, pw)

    # 打开一个通道
    chan = tran.open_session()
    # 获取一个终端
    chan.get_pty()
    # 激活器
    chan.invoke_shell()

    interactive_shell(chan)

    chan.close()
    tran.close()


if __name__ == '__main__':
    run()