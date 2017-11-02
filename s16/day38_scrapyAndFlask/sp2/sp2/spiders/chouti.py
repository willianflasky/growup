# -*- coding: utf-8 -*-
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from urllib.request import getproxies
import json
import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.http.cookies import CookieJar
from ..items import Sp2Item

# class ChoutiSpider(scrapy.Spider):
#     name = 'chouti'
#     allowed_domains = ['chouti.com']
#     cookies = None
#     cookie_dict = {}
#     start_urls = ['http://dig.chouti.com/',]
#
#     def index(self, response):
#         print('爬虫返回结果',response,response.url)

from scrapy_redis.spiders import RedisSpider
# class ChoutiSpider(RedisSpider):
#     name = 'chouti'
#     allowed_domains = ['chouti.com']
#
#     def index(self, response):
#         print('爬虫返回结果',response,response.url)

