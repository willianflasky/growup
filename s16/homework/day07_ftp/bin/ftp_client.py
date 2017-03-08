import os
import json
import struct
from socket import *
import hashlib
import sys

base_dir = os.path.normpath(os.path.join(__file__, os.pardir, os.pardir))
sys.path.insert(0, base_dir)
from lib import active
from conf import settings


class FtpClient:
    def __init__(self, ip, port, family=AF_INET, type1=SOCK_STREAM):
        self.client = socket(family, type1)
        self.client.connect((ip, port))

    def run(self):
        commands = ['get', 'put']
        while True:
            inp = input('>>: ').strip()
            if len(inp) == 0:
                continue
            elif inp == 'exit':
                break
            else:
                for command in commands:
                    if inp.startswith(command):
                        try:
                            cmd, attr = inp.split()
                        except ValueError as e:
                            print("example: {0} a.txt".format(inp))
                            break
                        if hasattr(self, cmd):
                            func = getattr(self, cmd)
                            func(attr)
                            break
                else:
                    if hasattr(self, 'cmd_process'):
                        func = getattr(self, 'cmd_process')
                        func(inp)

        self.client.close()

    def put(self, file_path):
        if os.path.exists(file_path):
            file_name = os.path.basename(file_path)  # c.txt
            file_size = os.path.getsize(file_path)   # c.txt size
            md5_value = active.md5sum(file_path)

            # 制作文件头部
            head_dict = {
                'cmd': 'put',
                'file_size': file_size,
                'file_name': file_name,
                'file_hash': md5_value,
            }

            # 将字典-->json-->bytes
            head_bytes = json.dumps(head_dict).encode('utf8')
            # 发送头部长度
            self.client.send(struct.pack('i', len(head_bytes)))
            # 发送头部
            self.client.send(head_bytes)
            with open(file_path, 'rb') as f2:
                for line in f2:
                    self.client.sendall(line)
        else:
            print("{0} not found!".format(file_path))

    def get(self, file_path):
        seek = 0
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                seek = file.seek(0, 2)

        head_dict = {
            'cmd': 'get',
            'file_path': file_path,
            'file_seek': seek,
        }
        # 发送4字节
        self.send_head(head_dict)
        # 收
        head4 = self.client.recv(4)
        head_size = struct.unpack('i', head4)[0]
        recv_head_dict = json.loads(self.client.recv(head_size).decode('utf8'))
        data_size = recv_head_dict['file_size']
        file = open('{0}'.format(os.path.basename(file_path)), 'wb')
        recv_size = 0
        while recv_size < data_size:
            ret = self.client.recv(settings.BUFFER_SIZE)
            file.write(ret)
            recv_size += len(ret)
        file.close()
        check_sum = active.md5sum(os.path.basename(file_path))
        if check_sum == recv_head_dict['file_hash']:
            print("\033[32;1m{0} download success.\033[0m".format(os.path.basename(file_path)))
        else:
            print("\033[31;1m{0} md5 check failure.\033[0m".format(os.path.basename(file_path)))

    def send_head(self, head_dict):  # cmd is /a/b.txt
        head_dict_bytes = json.dumps(head_dict).encode('utf8')
        self.client.send(struct.pack('i', len(head_dict_bytes)))
        self.client.send(head_dict_bytes)

    def cmd_process(self, cmd):     # ls
        head_dict = {
            'cmd': cmd,
        }
        self.send_head(head_dict)

        # -------收取结果--------
        # 收到头部长度
        header = self.client.recv(4)
        head_size = struct.unpack('i', header)[0]

        # 收头部
        head_bytes = self.client.recv(head_size)
        head_json = head_bytes.decode('utf8')
        headers = json.loads(head_json)

        # 获取真实数据长度
        data_size = headers['data_size']

        # 收取真实数据
        recv_size = 0
        recv_bytes = b''
        while recv_size < data_size:
            ret = self.client.recv(1024)
            recv_bytes += ret
            recv_size += len(ret)
        # 将结果打印
        print(str(recv_bytes, "utf8"))

    def __del__(self):
        self.client.close()

if __name__ == '__main__':
    f = FtpClient(settings.HOST, settings.PORT)
    f.run()
