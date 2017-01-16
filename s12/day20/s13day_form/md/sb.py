#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


from django.utils.deprecation import MiddlewareMixin

class M1(MiddlewareMixin):
    def process_request(self,request):
        print('M1.process_request')
    def process_response(self,request,response):
        print('M1.process_response')
        return response
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('m1.process_view')

class M2(MiddlewareMixin):
    def process_request(self,request):
        print('M2.process_request')
    def process_response(self,request,response):
        print('M2.process_response')
        return response
    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('m2.process_view')

