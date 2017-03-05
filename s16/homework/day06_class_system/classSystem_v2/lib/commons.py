#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import uuid
import hashlib
import time


def create_uuid():
    return str(uuid.uuid1())


if __name__ == '__main__':
    print(create_uuid())