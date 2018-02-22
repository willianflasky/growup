#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis


class BaseConfig(object):
    SESSION_TYPE = 'redis'  # session类型为redis
    SESSION_PERMANENT = False  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379', password='')  # 用于连接redis的配置


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass
