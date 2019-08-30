#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/3/19 下午3:34
__author__ = "willian"

# SESSION_ENGINE = "session_code.CacheSession"
SESSION_ENGINE = "session_code.RedisSession"
SESSION_ID = "__session__id__"
EXPIRES = 300
SESSION_HOST = "127.0.0.1"
SESSION_PORT = "6379"
