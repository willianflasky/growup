#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/19 下午3:07
__author__ = "willian"
import time
import hashlib
import settings
import redis
import json


# 生成随机字符串
def gen_random_str():
    md5 = hashlib.md5()
    md5.update(str(time.time()).encode('utf-8'))
    return md5.hexdigest()


# 基类
class SessionBase(object):
    def __init__(self, handler):
        self.handler = handler
        self.session_id = settings.SESSION_ID
        self.expires = settings.EXPIRES


# 写内存
class CacheSession(SessionBase):
    container = {}

    # handler相当于IndexHandler对象
    def __init__(self, handler):
        super(CacheSession, self).__init__(handler)
        self.initial()

    def initial(self):
        # 获取client的cookie
        client_random_str = self.handler.get_cookie(self.session_id)
        # 如果有值并且在container中能找到(才算合法)
        if client_random_str and client_random_str in self.container:
            self.random_str = client_random_str
        # 如果第一次访问没有cookie，则生成一个。存到container中
        else:
            self.random_str = gen_random_str()
            self.container[self.random_str] = {}
        # 刷新下过期时间
        exp = time.time() + self.expires
        self.handler.set_cookie(self.session_id, self.random_str, expires=exp)

    def __setitem__(self, key, value):
        self.container[self.random_str][key] = value

    def __getitem__(self, item):
        return self.container[self.random_str].get(item)

    def __delitem__(self, key):
        if key in self.container[self.random_str]:
            del self.container[self.random_str][key]


# 写redis
class RedisSession(SessionBase):
    def __init__(self, handler):
        super(RedisSession, self).__init__(handler)
        self.initial()

    @property
    def conn(self):
        conn = redis.Redis(host=settings.SESSION_HOST, port=settings.SESSION_PORT)
        return conn

    def initial(self):
        client_random_str = self.handler.get_cookie(self.session_id)

        if client_random_str and self.conn.exists(client_random_str):
            self.random_str = client_random_str
        else:
            self.random_str = gen_random_str()

        exp = time.time() + self.expires
        self.handler.set_cookie(self.session_id, self.random_str, expires=exp)
        self.conn.expire(self.random_str, self.expires)

    def __setitem__(self, key, value):
        self.conn.hset(self.random_str, key, json.dumps(value))

    def __getitem__(self, item):
        data_str = self.conn.hget(self.random_str, item)
        if data_str:
            return json.loads(data_str.decode('utf-8'))
        else:
            return None

    def __delitem__(self, key):
        self.conn.hdel(self.random_str, key)


class SessionFactory(object):
    @staticmethod
    def get_session():
        import settings
        import importlib
        engine = settings.SESSION_ENGINE
        module_path, cls_name = engine.rsplit('.', maxsplit=1)
        md = importlib.import_module(module_path)
        cls = getattr(md, cls_name)
        return cls
