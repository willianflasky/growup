#!/usr/bin/env python
#coding:utf8
#Author: willianflasky

import contextlib

@contextlib.contextmanager
def worker_state(status_list,worker_thread):
    status_list.append(worker_thread)
    try:
        yield
    finally:
        status_list.remove(worker_thread)

free_list=[]
current_thread='alex'
with worker_state(free_list,current_thread):
    print(123)
    print(456)
