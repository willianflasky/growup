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
    ch.basic_ack(delivery_tag=method.delivery_tag)
channel.basic_qos(prefetch_count=1)         # 默认消息队列里的数据是按照顺序被消费者拿走，
                                            # 例如：消费者1 去队列中获取 奇数 序列的任务，消费者1去队列中获取 偶数 序列的任务。
                                            # 表示谁来谁取，不再按照奇偶数排列
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)

channel.start_consuming()
