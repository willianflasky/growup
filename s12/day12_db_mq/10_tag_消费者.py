#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='10.211.55.5'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

#type=topic 可以实现模糊匹配, #表示匹配0个多个字符,*表示只匹配一个字符.


result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

severities=['error','info','warning']


for severity in severities:
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()