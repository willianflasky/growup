#!/usr/local/bin/python3
#decoding=utf8

import socket
import os
import json
import optparse
import getpass
import hashlib
import sys
import struct

STATUS_CODE = {
    250: "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251: "Invalid cmd ",
    252: "Invalid auth data",
    253: "Wrong username or password",
    254: "Passed authentication",
}


class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="ftp server ip address")
        parser.add_option("-P", "--port", type="int", dest="port", help="ftp server port")
        parser.add_option("-u", "--username", dest="username", help="username")
        parser.add_option("-p", "--password", dest="password", help="password")
        self.options, self.args = parser.parse_args()
        self.verify_args(self.options, self.args)
        self.make_connection()

    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server, self.options.port))

    def verify_args(self, options, args):
        if options.username is not None and options.password is not None:
            pass
        elif options.username is None and options.password is None:
            pass
        else:
            # options.username is None or options.password is None:
            exit("Err: username and password must be provided together..")

        if options.server and options.port:
            if options.port > 0 and options.port < 65535:   # 验证端口号
                return True
            else:
                exit("Err:host port must in 0-65535")

    def authenticate(self):
        if self.options.username:
            print(self.options.username, self.options.password)
            return self.get_auth_result(self.options.username, self.options.password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username:").strip()
                password = input("password:").strip()
                return self.get_auth_result(username, password)

    def get_auth_result(self, user, password):
        data = {'action': 'auth',
                'username': user,
                'password': password}

        self.sock.send(json.dumps(data).encode())
        response = self.get_response()
        if response.get('status_code') == 254:
            print("Passed authentication!")
            self.user = user
            return True
        else:
            print(response.get("status_msg"))

    def get_response(self):
        data = self.sock.recv(1024)
        # print("server res", data)
        data = json.loads(data.decode())
        return data

    def interactive(self):
        if self.authenticate():
            print("---start interactive with u...")
            while True:
                choice = input("[%s]:" % self.user).strip()
                if len(choice) == 0:
                    continue
                cmd_list = choice.split()
                if hasattr(self, "_%s" % cmd_list[0]):
                    func = getattr(self, "_%s" % cmd_list[0])
                    func(cmd_list)
                else:
                    print("Invalid cmd.")

    def __md5_required(self, cmd_list):
        if '--md5' in cmd_list:
            return True

    def show_progress(self, total):
        received_size = 0 
        current_percent = 0 
        while received_size < total:
            if int((received_size / total) * 100) > current_percent:
                print("#", end="", flush=True)
                current_percent = int((received_size / total) * 100)
            new_size = yield
            received_size += new_size

    def _get(self, cmd_list):
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        data_header = {
            'action': 'get',
            'filename': cmd_list[1]
        }

        if self.__md5_required(cmd_list):
            data_header['md5'] = True

        self.sock.send(json.dumps(data_header).encode())  # 发送header
        response = self.get_response()                    # 接收响应
        print(response)
        if response["status_code"] == 257:       # ready to receive
            self.sock.send(b'1')                 # send confirmation to server
            base_filename = os.path.basename(cmd_list[1])
            received_size = 0
            file_obj = open(base_filename, "wb")
            if self.__md5_required(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_progress(response['file_size'])    # generator
                progress.__next__()
                while received_size < response['file_size']:
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        print("100%")
                    file_obj.write(data)
                    md5_obj.update(data)
                else:
                    print("----->file rece done----")
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    md5_from_server = self.get_response()
                    if md5_from_server['status_code'] == 258:
                        if md5_from_server['md5'] == md5_val:
                            print("%s 文件一致性校验成功!" % base_filename)
                    # print(md5_val,md5_from_server)
            else:
                progress = self.show_progress(response['file_size'])    # generator
                progress.__next__()     # 让它停在yield

                while received_size < response['file_size']:
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    file_obj.write(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e:
                        print("100%")
                else:
                    print("----->file rece done----")
                    file_obj.close()

    def _put(self, cmd_list):
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        data_header = {'action': 'put', 'filename': cmd_list[1]}

        if os.path.isfile(cmd_list[1]):
            md5_val = self.md5sum(cmd_list[1])
            file_size = os.path.getsize(cmd_list[1])
            data_header['md5sum'] = md5_val
            data_header['file_size'] = file_size,
        else:
            if os.path.isdir(cmd_list[1]):
                print("not support dir.")
            else:
                print("\033[31;1m请检查文件是否存在.\033[0m")
            return

        self.sock.send(json.dumps(data_header).encode())

        recv_res = self.to_recv()
        if recv_res == '259':
            print("\033[31;1m文件已经存在服务上.\033[0m")
            return
        elif recv_res == 'too_big':
            print("\033[31;1m文件太大,超过限制.\033[0m")
            return
        elif recv_res == '257':
            with open(cmd_list[1], 'rb') as f:
                data = f.read()
            self.to_send(data)
            ack = self.to_recv()
            if ack == '258':
                print("\033[32;1mtransfer done and md5sum ok.\033[0m")
            else:
                print("\033[31;1mtransfer done but md5sum {0}\033[0m".format(ack))
            return

    def _ls(self, cmd):
        data_header = {
            'action': cmd[0],
            'username': self.user,
        }
        self.sock.send(json.dumps(data_header).encode())
        data = self.to_recv()
        print(data)

    def _pwd(self, cmd):
        data_header = {
            'action': cmd[0],
            'username': self.user,
        }
        self.sock.send(json.dumps(data_header).encode())
        data = self.to_recv()
        print(data)

    def _help(self, cmd):
        data_header = {
            'action': cmd[0],
            'username': self.user,
        }
        self.sock.send(json.dumps(data_header).encode())
        data = self.to_recv()
        print("\033[32;1m{0}\033[0m".format(data))

    def _cd(self, cmd_list):
        data_header = {
            'action': cmd_list[0],
            'username': self.user,
            'cmd_list': cmd_list,
        }
        self.sock.send(json.dumps(data_header).encode())
        data = self.to_recv()
        print("\033[32;1m{0}\033[0m".format(data))

    def to_send(self, data):
        # 第一, 制作头部
        headers = {'data_size': len(data)}
        headers_bytes = bytes(json.dumps(headers).encode('utf8'))
        # 第二, 发送报头长度
        self.sock.send(struct.pack('i', len(headers_bytes)))
        # 第三, 发送报头
        self.sock.send(headers_bytes)
        # 第四, 发送数据
        self.sock.sendall(data)

    def to_recv(self):
        # 收到头部长度
        header = self.sock.recv(4)
        head_size = struct.unpack('i', header)[0]
        # 收头部
        headers = str(self.sock.recv(head_size).decode('utf8'))
        headers = json.loads(headers)

        # 获取真实数据长度
        data_size = headers['data_size']
        # 收取真实数据
        recv_size = 0
        recv_bytes = b''
        while recv_size < data_size:
            ret = self.sock.recv(4096)
            recv_bytes += ret
            recv_size += len(ret)
        return str(recv_bytes, "utf8")

    def md5sum(self, file):
        if os.path.exists(file):
            with open(file, 'rb') as f1:
                m = hashlib.md5()
                m.update(f1.read())
                return m.hexdigest()
        else:
            return None

if __name__ == "__main__":
    ftp = FTPClient()
    ftp.interactive()