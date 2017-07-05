#!/usr/bin/env python
#-*- coding: utf-8 -*-
# by Wendy

#_*_coding:utf-8_*_
__author__ = 'Alex Li'

#关于直接带一个user 一个timestamp和md5的值,安全还咩有到那么高
#但是还需要有认证就可以用这个

#后端服务器还需要积累一个md5的库然后来对比如果有的话就不是第一次访问
#库里面没有就第一次访问的

#并且设置有效时间 5分钟之内 就检查md5 如果超过5分钟就干掉


import time,hashlib,json
from assets import models
from django.shortcuts import render,HttpResponse
#from s16MadKing import settings
from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist
def json_date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.strftime("%Y-%m-%d")


def json_datetime_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.strftime("%Y-%m-%d %H:%M:%S")


def gen_token(username,timestamp,token):
    token_format = "%s\n%s\n%s" %(username,timestamp,token)
    #print('--->token format:[%s]'% token_format)

    obj = hashlib.md5()
    obj.update(token_format.encode())
    return obj.hexdigest()[10:17]

#api安全的装饰器
def token_required(func):

#1、取认证参数
#2、根据时间戳,判断请求是否过期
#3、算出md5 , 与客户端md5比较
#4、判断是否是第一次请求

    def wrapper(*args,**kwargs):
        response = {"errors":[]}

        #qu
        request = args[0]
        get_args = args[0].GET #request
        username = get_args.get("user")
        token_md5_from_client = get_args.get("token")
        timestamp = get_args.get("timestamp")

        if not username or not timestamp or not token_md5_from_client:
            response['errors'].append({"auth_failed":"This api requires token authentication!"})
            return HttpResponse(json.dumps(response))
        try:
            user_obj = models.UserProfile.objects.get(user__username=username)
            token_md5_from_server = gen_token(username,timestamp,user_obj.token)
            if token_md5_from_client != token_md5_from_server:
                response['errors'].append({"auth_failed":"Invalid username or token_id"})
            else:
                if abs(time.time() - int(timestamp)) > settings.TOKEN_TIMEOUT:# default timeout 120
                    response['errors'].append({"auth_failed":"The token is expired!"})
                else:
                    pass #print "\033[31;1mPass authentication\033[0m"

                print("\033[41;1m;%s ---client:%s\033[0m" %(time.time(),timestamp), time.time() - int(timestamp))
        except ObjectDoesNotExist as e:
            response['errors'].append({"auth_failed":"Invalid username or token_id"})
        if response['errors']:
            return HttpResponse(json.dumps(response))
        else:
            return  func(*args,**kwargs)
    return wrapper



