#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import pika
import json
import threading
from lib import base


class recver(base.BASE):
    def __init__(self):
        super(recver, self).__init__()

    def exchange(self, group):
        result = self.channel.queue_declare(exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.name, queue=self.queue_name, routing_key=group)

    def callback(self, ch, method, properties, body):
        # print("[recver] %r:%r" % (method.routing_key, body))
        body_dic = json.loads(body.decode('utf8'))
        print("\033[31;1m{0}:\033[0m".format(body_dic['host']))
        print("\033[34;1m{0}\033[0m".format(body_dic['result']))

    def run(self):
        self.channel.basic_consume(self.callback, queue=self.queue_name, no_ack=True)
        self.channel.start_consuming()

    def close(self):
        self.channel.close()
        self.connection.close()
