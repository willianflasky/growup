#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import socketserver
import subprocess
import http.server

MyServer=http.server.BaseHTTPRequestHandler



if __name__ == '__main__':
    server=socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
    server.serve_forever()