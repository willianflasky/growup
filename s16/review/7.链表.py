#!/usr/bin/env python
# -*-coding:utf8-*-
__author__ = "willian"


# 一、简单链表

class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = Node


a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c


# print(a.next.item)
# 遍历链表

def traversal(head):
    curr_node = head
    while curr_node is not Node:
        print(curr_node.item)
        curr_node = curr_node.next


traversal(b)

# 二、链表节点的插入和删除(插入和删除比列表快)

# 插入
"""
    p.next = curr_node.next
    curr_node.next = p
"""

# 删除
"""
    p = curr_node.next
    curr_node.next = p.next
    del p
"""


# 新建链表
# 1.头插发

def create_link_list_left(li):
    ll = Node()
    for num in li:
        s = Node(num)
        s.next = ll.next
        ll.next = s
    return ll


def create_link_list_right(li):
    ll = Node()
    r = ll
    for num in li:
        s = Node(num)
        r.next = s
        r = s

# 三、双链表
