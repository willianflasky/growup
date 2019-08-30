import socketserver


class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            pass

    def put(self):
        pass


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8080), FtpServer)
    s.serve_forever()
