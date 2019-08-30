import os
import json
import struct
from socket import *


class FtpClient:
    def __init__(self, ip, port, family=AF_INET, type1=SOCK_STREAM):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((ip, port))

    def run(self):
        while True:
            inp = input('>>: ').strip()
            if not cmd:
                continue
            cmd, attr = inp.split()     # put /a/b/c/a.txt
            if hasattr(self, cmd):
                func = getattr(self, cmd)
                func(attr)

    def put(self, filepath):
        filename = os.path.basename(filepath)
        filesize = os.path.getsize(filepath)
        head_dict = {
            'cmd': 'put',
            'filesize': filesize,
            'filename': filename
        }
        head_json = json.dumps(head_dict)
        head_bytes = head_json.encode('utf-8')

        self.client.send(struct.pack('i', len(head_bytes)))
        self.client.send(head_bytes)
        with open(filepath, 'rb') as f1:
            for line in f1:
                self.client.send(line)


if __name__ == '__main__':
    f = FtpClient('127.0.0.1', 8080)
    f.run()
