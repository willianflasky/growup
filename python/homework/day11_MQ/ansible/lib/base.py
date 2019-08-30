#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import pika
from conf import settings


class BASE(object):
    def __init__(self, host=settings.rabbit_server, name=settings.rabbit_exchange, type1='direct'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.name = name
        self.channel.exchange_declare(exchange=self.name, type=type1)

