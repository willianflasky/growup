# from scrapy.utils.request import request_fingerprint
# from scrapy.http import Request
#
#
# obj1 = Request(url='http://www.baidu.com?a=1&b=2',headers={'Content-Type':'application/text'},callback=lambda x:x)
# obj2 = Request(url='http://www.baidu.com?b=2&a=1',headers={'Content-Type':'application/json'},callback=lambda x:x)
#
# v1 = request_fingerprint(obj1,include_headers=['Content-Type'])
# print(v1)
#
# v2 = request_fingerprint(obj2,include_headers=['Content-Type'])
# print(v2)


# li = [11,22,33]



# 迭代器，具有__next__方法，并逐一向后取值
# li = [11,22,33]
# obj = iter(li)
# obj.__next__()

# 可迭代对象，具有__iter__方法，返回迭代器
# li = list([11,22,33])
# 迭代器 = li.__iter__()

# 生成器，函数中具有yield关键字
# __iter__
# __next__

# 迭代器 = iter(obj)

