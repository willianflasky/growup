#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback, queue='hello', no_ack=False)
# no_ack: acknowledgment 消息不丢失,MQ判读出现异常,没有消费,没有ack,则把消息放回队列.
channel.start_consuming()

