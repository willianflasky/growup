#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.3.6'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
