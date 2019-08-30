#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import os
import sys
import logging
base_dir = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir, os.pardir,))
DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': "%s/atm/db" % base_dir
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0},
}

