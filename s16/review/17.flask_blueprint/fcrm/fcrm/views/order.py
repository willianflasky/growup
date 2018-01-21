#!/usr/bin/env python
# -*-coding:utf8-*-
# date: 2018/1/21 下午5:17
__author__ = "willian"


from flask import Blueprint

order = Blueprint('order', __name__)


@order.route("/order")
def xx():
    return "order"
