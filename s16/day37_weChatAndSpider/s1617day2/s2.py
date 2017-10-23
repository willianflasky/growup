import socket
import select

class Request(object):
    def __init__(self,sock,func,url):
        self.sock = sock
        self.func = func
        self.url = url

    def fileno(self):
        return self.sock.fileno()

def async_request(url_list):

    input_list = []
    conn_list = []

    for url in url_list:
        client = socket.socket()
        client.setblocking(False)
        # 创建连接,不阻塞
        try:
            client.connect((url[0],80,)) # 100个向百度发送的请求
        except BlockingIOError as e:
            pass

        obj = Request(client,url[1],url[0])

        input_list.append(obj)
        conn_list.append(obj)

    while True:
        # 监听socket是否已经发生变化 [request_obj,request_obj....request_obj]
        # 如果有请求连接成功：wlist = [request_obj,request_obj]
        # 如果有响应的数据：  rlist = [request_obj,request_obj....client100]
        rlist,wlist,elist = select.select(input_list,conn_list,[],0.05)
        for request_obj in wlist:
            # print('连接成功')
            # # # # 发送Http请求
            # print('发送请求')
            request_obj.sock.sendall("GET / HTTP/1.0\r\nhost:{0}\r\n\r\n".format(request_obj.url).encode('utf-8'))
            conn_list.remove(request_obj)

        for request_obj in rlist:
            data = request_obj.sock.recv(8096)
            request_obj.func(data)
            request_obj.sock.close()
            input_list.remove(request_obj)

        if not input_list:
            break






