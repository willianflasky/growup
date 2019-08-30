#!/usr/bin/python
# -*- coding:utf-8 -*-

import re



ret=re.search(r"(?P<year>\d{4})/(?P<month>\d{2})/(?P<id>\d{2})",r"2009/12/08")

print(ret.group("year"))