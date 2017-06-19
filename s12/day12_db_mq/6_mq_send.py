#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='10.211.55.5'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2
                      ))
# properties=pika.BasicProperties(delivery_mode=2) 增加持久化功能

print(" [x] Sent 'Hello World!'")
connection.close()

#durable=True 声明了队列需要持久化，delivery_mode = 2 声明了队列的消息需要持久化。

