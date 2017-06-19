#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

from wsgiref.simple_server import make_server


def RunServer(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return '<h1>Hello,web!</h1>'

if __name__=='__main__':
	httpd = make_server('',8000,RunServer)
	print("Serving HTTP on port 8000...")
	httpd.serve_forever()