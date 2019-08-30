import socketserver
class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request) #conn
        print(self.client_address)
        while True:
            data=self.request.recv(1024)
            self.request.send(data.upper())

if __name__ == '__main__':
    s=socketserver.ThreadingTCPServer(('127.0.0.1',8080),FtpServer)
    s.serve_forever() #链接循环有了

