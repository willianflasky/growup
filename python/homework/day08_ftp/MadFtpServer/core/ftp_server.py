import socketserver
import configparser
from conf import settings
import os
import hashlib
import json
import subprocess
import struct
import re


STATUS_CODE = {
    250: "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251: "Invalid cmd ",
    252: "Invalid auth data",
    253: "Wrong username or password",
    254: "Passed authentication",
    255: "Filename doesn't provided",
    256: "File doesn't exist on server",
    257: "ready to send file",
    258: "md5 verification",
    259: "File exist on server",

}


class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            if not self.data:
                print("client closed...")
                break
            data = json.loads(self.data.decode())
            if data.get('action') is not None:
                print("---->", hasattr(self, "_auth"))
                if hasattr(self, "_%s" % data.get('action')):
                    func = getattr(self, "_%s" % data.get('action'))
                    func(data)
                else:
                    print("invalid cmd")
                    self.send_response(251)
            else:
                print("invalid cmd format")
                self.send_response(250)

    def send_response(self, status_code, data=None):
        response = {'status_code': status_code, 'status_msg': STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())

    def _auth(self, *args, **kwargs):
        data = args[0]
        if data.get("username") is None or data.get("password") is None:
            self.send_response(252)

        user = self.authenticate(data.get("username"), data.get("password"))
        if user is None:
            self.send_response(253)
        else:
            print("passed authentication", user)
            self.user = user
            self.user['username'] = data.get("username")

            self.home_dir = "%s/home/%s" % (settings.BASE_DIR, data.get("username"))
            self.current_dir = self.home_dir
            self.send_response(254)

    def authenticate(self, username, password):
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == password:
                print("pass auth..", username)
                config[username]["Username"] = username
                return config[username]

    def _put(self, *args, **kwargs):
        # args = ({'action': 'put', 'filename': 'dir/b.txt'},)
        data = args[0]
        file_name = os.path.basename(data['filename'])
        real_path_file_name = os.path.join(self.current_dir, file_name)
        if os.path.exists(real_path_file_name):
            self.to_send(bytes("259", encoding='utf8'))
        else:
            current_size = self.getdirsize(self.home_dir)
            quotation = int(self.user['Quotation']) * 1000000
            if (current_size + data['file_size'][0]) < quotation:
                self.to_send(bytes("257", encoding='utf8'))
            else:
                self.to_send(bytes("too_big", encoding='utf8'))
                return
            recv_data = self.to_recv()
            if recv_data:
                with open('{0}/{1}'.format(self.current_dir, file_name), 'wb') as f:
                    # f.write(bytes(recv_data, encoding='utf8'))
                    f.write(recv_data)
            md5_val = self.md5sum(real_path_file_name)
            if data['md5sum'] == md5_val:
                self.to_send(bytes('258', encoding='utf8'))
            else:
                self.to_send(bytes('err', encoding='utf8'))

    def _get(self, *args, **kwargs):
        data = args[0]
        if data.get('filename') is None:
            self.send_response(255)
        user_home_dir = "%s/%s" % (settings.USER_HOME, self.user["Username"])
        file_abs_path = "%s/%s" % (user_home_dir, data.get('filename'))
        print("file abs path", file_abs_path)

        if os.path.isfile(file_abs_path):
            file_obj = open(file_abs_path, "rb")
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257, data={'file_size': file_size})
            self.request.recv(1)    # 等待客户端确认

            if data.get('md5'):
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    self.send_response(258, {'md5': md5_val})
                    print("send file done....")
            else:
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print("send file done....")
        else:
            self.send_response(256)

    def _ls(self, *args, **kwargs):
        list_dir = subprocess.Popen("ls  -lsh {0} ".format(self.current_dir), shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        res = list_dir.stdout.read()
        self.to_send(res)

    def _cd(self, *args, **kwargs):
        # ({'cmd_list': cmd_list, action': 'cd', 'username': 'alex'},)
        relative_dir = self.calc_path(self.current_dir)     # /home/alex

        if len(args[0]['cmd_list']) == 1:
            dest_path = self.home_dir
        else:
            dest_path = os.path.join(self.home_dir, args[0]['cmd_list'][1])

        if dest_path.startswith(self.home_dir) and os.path.isdir(dest_path):
            self.current_dir = dest_path
            self.to_send(bytes("path changed", encoding='utf8'))
        else:
            self.to_send(bytes("no permission", encoding='utf8'))

    def _pwd(self, *args, **kwargs):
        self.to_send(bytes(self.calc_path(self.current_dir), encoding='utf8'))

    def _help(self, *args, **kwargs):
        msg = "支持命令:get put ls cd pwd\n"
        self.to_send(bytes(msg, encoding='utf8'))

    def to_send(self, data):
        # 第一, 制作头部
        headers = {'data_size': len(data)}
        headers_bytes = bytes(json.dumps(headers).encode('utf8'))
        # 第二, 发送报头长度
        self.request.send(struct.pack('i', len(headers_bytes)))
        # 第三, 发送报头
        self.request.send(headers_bytes)
        # 第四, 发送数据
        self.request.sendall(data)

    def to_recv(self):
        # 收到头部长度
        header = self.request.recv(4)
        head_size = struct.unpack('i', header)[0]
        # 收头部
        headers = str(self.request.recv(head_size).decode('utf8'))
        headers = json.loads(headers)

        # 获取真实数据长度
        data_size = headers['data_size']
        # 收取真实数据
        recv_size = 0
        recv_bytes = b''
        while recv_size < data_size:
            ret = self.request.recv(4096)
            recv_bytes += ret
            recv_size += len(ret)
        # return str(recv_bytes, "utf8")
        return recv_bytes

    def calc_path(self, args):
        pwd = re.sub(settings.BASE_DIR, "", args, 1)
        return pwd

    def md5sum(self, file):
        if os.path.exists(file):
            with open(file, 'rb') as f1:
                m = hashlib.md5()
                m.update(f1.read())
                return m.hexdigest()
        else:
            return None

    def getdirsize(self, dir):
       size = 0
       for root, dirs, files in os.walk(dir):
          size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
       return size

if __name__ == "__main__":
    HOST, PORT = "localhost", 9000
