#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='127.0.0.1', port=5672))
channel = connection.channel()

channel.queue_declare(queue='hello')        # 创建通道

channel.basic_publish(exchange='',
                      routing_key='hello',  # 关键字
                      body='Hello World!')  # 信息
connection.close()

