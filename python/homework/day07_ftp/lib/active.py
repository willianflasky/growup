#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import hashlib
import os
from conf import settings
import json
import struct


def md5sum(file):
    if os.path.exists(file):
        with open(file, 'rb') as f1:
            m = hashlib.md5()
            m.update(f1.read())
            return m.hexdigest()
    else:
        return None


def put(conn, cmd, file_size, file_name, file_hash):
    f = open(file_name, 'wb')
    recv_size = 0
    while recv_size < file_size:
        ret = conn.recv(settings.BUFFER_SIZE)
        f.write(ret)
        recv_size += len(ret)
    f.close()
    check_sum = md5sum(file_name)
    if check_sum == file_hash:
        print("{0} upload success.".format(file_name))
    else:
        print("{0} md5 check failure as soon as remove it.")
        os.remove(file_name)


def get(conn, cmd, file_path, file_seek):
    if os.path.exists(file_path):
        md5_value = md5sum(file_path)
        file_size = os.path.getsize(file_path)
        if file_size == file_seek:
            head_dict = {
                "file_hash": md5_value,
                'file_size': 0,
            }
            send_head(conn, head_dict)
            return
        if file_seek != 0 and file_size > file_seek:
            file_size = file_size - file_seek

        head_dict = {
            "file_hash": md5_value,
            'file_size': file_size,     # 138
        }
        # 发送头长度和头部字典
        send_head(conn, head_dict)

        with open(file_path, 'rb') as fx:
            fx.seek(file_seek)
            data = fx.read()
            conn.sendall(data)


def send_head(conn, head_dict):
    head_dict_bytes = json.dumps(head_dict).encode('utf8')
    conn.send(struct.pack('i', len(head_dict_bytes)))
    conn.send(head_dict_bytes)
