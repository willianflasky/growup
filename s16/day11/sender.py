#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import uuid
import pika
import sys
import threading



class sender(object):
    def __init__(self, host='localhost', name='ansible'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.name = name

    def exchange(self, type1='direct'):
        self.channel.exchange_declare(exchange=self.name, type=type1)

    def run(self, group, cmd, my_uuid=uuid.uuid4()):
        message = '{"id":"%s","cmd":"%s"}' % (my_uuid, cmd)
        self.channel.basic_publish(exchange=self.name, routing_key=group, body=message)
        print("[Sent] %s:%s" % (group, message))
        print(type(message))

    def run_back(self, uuid, result):
        self.channel.basic_publish(exchange=self.name, routing_key=uuid, body=result)

    def __del__(self):
        self.connection.close()


if __name__ == '__main__':

    s1 = sender('localhost')
    s1.exchange()

    while True:
        cmd = input('cmd:').strip()
        s1.run('webserver', cmd)




