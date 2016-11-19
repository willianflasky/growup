#!/usr/bin/env python
#coding:utf8
#Author: willianflasky


import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.3.6'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severity='error'
message='123'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()