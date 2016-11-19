#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import queue
#queue.Queue #FIFO
#queue.LifoQueue #后进先出
#queue.PriorityQueue #优先级队列
#queue.deque #双向对列

"""
q=queue.Queue(2)
print(q.empty())
q.put(11)
q.put(22)
print(q.empty())
print(q.qsize())

#q.put(33,timeout=2)
q.put(33,block=False)

print(q.qsize())
print(q.get(timeout=2))

"""
q=queue.LifoQueue()
q.put(123)
q.put(456)
print(q.get())

q=queue.PriorityQueue()
q.put(0,'q0')
q.put(100,'q100')
q.put(1,'q1')
print(q.get())
print(q.get())

q=queue.deque()
q.append(123)
q.append(333)
q.appendleft(1111)
q.pop()
q.popleft()
