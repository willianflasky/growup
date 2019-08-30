#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import pika
import uuid
from lib import base


class sender(base.BASE):
    def __init__(self):
        super().__init__()

    def run(self, group, cmd, my_uuid=uuid.uuid4()):
        message = '{"id":"%s","cmd":"%s"}' % (my_uuid, cmd)
        self.channel.basic_publish(exchange=self.name, routing_key=group, body=message)
        # print("[Sent] %s:%s" % (group, message))

    def close(self):
        self.connnection.close()
