#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='127.0.0.1', port=5672))
channel = connection.channel()

channel.queue_declare(queue='hello1', durable=True)        # 创建通道, 持久化修改1:durable=True

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!',
                      properties=pika.BasicProperties(delivery_mode=2)  # 持久化修改2
                      )
connection.close()

