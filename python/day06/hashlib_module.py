#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import hashlib
import hmac


s = hashlib.sha512()
print(s.hexdigest())
