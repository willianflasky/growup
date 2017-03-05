#!/usr/bin/env python
# -*-coding:utf8-*-
# __author__ = "willian"

import re


# 从头匹配,很少使用
re.match("\d+", "341221")
# 匹配一次
re.search("\d+", "341221")
# 匹配多次
re.findall("\d+", "341221")
# 以逗号分割
re.split(",", "341,221")
# 匹配到进行替换,默认是替代所有,count指定次数.
re.sub("\d{4}", "1995", "1399,2017", count=1)

# re.I  (忽略大小写)
# print(re.search("[a-z]", "Alex", flags=re.I))
# re.M  (匹配多行)
# print(re.search("^is", "my name\nis alex", flags=re.M))
# re.S  (多行匹配在一起)
# print(re.search(".+", "my \nname", flags=re.S))

