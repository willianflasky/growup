#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    import time
    time.sleep(10)
    print('ok')
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 持久化:修改2

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)         # 持久化:修改1

channel.start_consuming()
