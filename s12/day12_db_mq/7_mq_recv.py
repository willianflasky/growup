#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='10.211.55.5'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True


def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body))
    import time
    time.sleep(10)
    print('ok')
    ch.basic_ack(delivery_tag= method.delivery_tag)

channel.basic_qos(prefetch_count=1) #表示按顺序拿数据,不按奇偶

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)  #false表示,没有ack,则重新放在队列中.

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()