#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import os
import sys
from optparse import OptionParser
import pika
import uuid
import json
import subprocess
import threading
import socket

parser = OptionParser()
parser.add_option("-i", "--ip", default='localhost', help="rabbit server addr, default=localhost")
parser.add_option("-n", "--name", default='ansible', help="rabbit exchange name, default=ansible")
(options, args) = parser.parse_args()

options_dic = (eval(str(options)))


class BASE(object):
    def __init__(self, host=options_dic['ip'], name=options_dic['name'], type1='direct'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.name = name
        self.channel.exchange_declare(exchange=self.name, type=type1)


class sender(BASE):
    def __init__(self):
        super().__init__()

    def run_back(self, uuid, result):
        self.channel.basic_publish(exchange=self.name, routing_key=uuid, body=result)

    def __del__(self):
        self.connection.close()


class recver(BASE):
    def __init__(self):
        super(recver, self).__init__()

    def exchange(self, group):
        result = self.channel.queue_declare(exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.name, queue=self.queue_name, routing_key=group)

    def callback(self, ch, method, properties, body):
        print("[recver] %r:%r" % (method.routing_key, body))
        body_str = body.decode('utf8')
        body_dict = json.loads(body_str)
        res = subprocess.Popen(body_dict['cmd'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = res.stdout.read()
        if result:
            print(result)
        else:
            result = res.stderr.read()
            print(result)

        hostname = socket.gethostname()
        # ip = socket.gethostbyname(hostname)
        info = {'host': hostname, 'result': result.decode('utf8')}  # dict
        info = json.dumps(info).encode('utf8')  # dict --> json(str) --> bytes
        toback = sender()
        toback.run_back(body_dict['id'], info)
        print("\033[31;1mto back done!\033[0m")
        self.channel.stop_consuming()

    def run(self):
        self.channel.basic_consume(self.callback, queue=self.queue_name, no_ack=True)
        self.channel.start_consuming()

    def close(self):
        self.channel.close()
        self.connection.close()


if __name__ == '__main__':
    while True:
        r1 = recver()
        r1.exchange('webserver')
        r1.run()
        r1.close()

