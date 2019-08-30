#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import uuid
import pika
import sys
import json
import threading
import sender
import subprocess


def proces(cmd):
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.stderr:
        return res.stderr.read()
    else:
        return res.stdout.read()


class recver(object):
    def __init__(self, host, name='ansible'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.name = name

    def exchange(self, group, type1='direct'):
        self.channel.exchange_declare(exchange=self.name, type=type1)
        result = self.channel.queue_declare(exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.name, queue=self.queue_name, routing_key=group)

    def callback(self, ch, method, properties, body):
        print("[recver] %r:%r" % (method.routing_key, body))
        body_str = body.decode('utf8')
        body_dict = json.loads(body_str)
        result = proces(body_dict['cmd'])
        send = sender.sender()
        send.exchange()
        t = threading.Thread(send.run_back, args=(body_dict['id'], result))
        t.start()

    def run(self):
        self.channel.basic_consume(self.callback, queue=self.queue_name, no_ack=True)
        self.channel.start_consuming()

    def __del__(self):
        self.channel.close()
        self.connection.close()

r1 = recver('localhost')
r1.exchange('webserver')
r1.run()




