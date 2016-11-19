#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

#发布者

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='10.211.55.5'))
channel = connection.channel()

channel.exchange_declare(exchange='logs_fanout',
                         type='fanout')

message = '456'
channel.basic_publish(exchange='logs_fanout',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()