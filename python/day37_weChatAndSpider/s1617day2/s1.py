# 1. 100张图片，下载图片
# import requests
# url_list = ['http://www.baid.com',] # 10s
# for url in url_list:
#     requests.get(url)

# 2. 线程池或进程池提高并发，资源的浪费
# py2: 无线程池,有进程池
# py3: 有线程池,有进程池
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import requests
# def task(url):
#     response = requests.get(url)
#     print(response.content)
#
# # 最多创建10个线程
# pool = ThreadPoolExecutor(10) # 线程池
# # pool = ProcessPoolExecutor(10) # 进程池
# url_list = ['http://www.baidu.com','http://www.bing.com',] # 10s
# for url in url_list:
#     v = pool.submit(task,url)
# pool.shutdown(wait=True)

# 3. 异步非阻塞，1一个线程完成并发操作
"""
    非阻塞: 不等
      异步：回调
"""
# import asyncio
#
#
# @asyncio.coroutine
# def fetch_async(host, url='/'):
#     print(host, url)
#     reader, writer = yield from asyncio.open_connection(host, 80)
#
#     request_header_content = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host,)
#     request_header_content = bytes(request_header_content, encoding='utf-8')
#
#     writer.write(request_header_content)
#     yield from writer.drain()
#     text = yield from reader.read()
#     print(host, url, text)
#     writer.close()
#
# task_list = [
#     fetch_async('www.cnblogs.com', '/wupeiqi/'),
#     fetch_async('dig.chouti.com', '/pic/show?nid=4073644713430508&lid=10273091')
# ]
#
# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(asyncio.gather(*task_list))
# loop.close()





import asyncio
import requests


# @asyncio.coroutine
# def fetch_async(func, *args):
#     loop = asyncio.get_event_loop()
#     future = loop.run_in_executor(None, func, *args)
#     response = yield from future
#     print(response.url, response.content)
#
#
# tasks = [
#     fetch_async(requests.get, 'http://www.cnblogs.com/wupeiqi/'),
#     fetch_async(requests.get, 'http://dig.chouti.com/pic/show?nid=4073644713430508&lid=10273091')
# ]
#
# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()










