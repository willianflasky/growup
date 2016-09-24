#!/usr/bin/env python
#coding:utf8
#Author: willianflasky
import redis

class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')

    def public(self, msg,chan):
        self.__conn.publish(chan, msg)
        return True

    def subscribe(self,chan):
        pub = self.__conn.pubsub()
        pub.subscribe(chan)
        pub.parse_response()
        return pub






