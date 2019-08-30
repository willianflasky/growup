# -*- coding: utf-8 -*-
import scrapy
import io
import sys
# 解决windows乱码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

# 解析模块
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http.cookies import CookieJar
from scrapy.http import Request


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response):
        """
        1. 获取想要的内容
        2. 如果有分页继续下载页面
        """
        # bytes格式
        # print(type(response.body))

        # str格式
        # print(response.text)
        # 开始解析,转换成对象
        hxs = Selector(response=response)
        # //找子孙, /找儿子
        # 每条新闻
        item_list = hxs.xpath('//div[@id="content-list"]/div[@class="item"]')
        # print(item_list[0])
        # ./表示当前对象下面找
        for item in item_list:
            from ..items import Sp2Item
            title = item.xpath('./div[@class="news-content"]//a[@class="show-content"]/text()').extract_first()
            href = item.xpath('./div[@class="news-content"]//a[@class="show-content"]/@href').extract_first()
            item_obj = Sp2Item(title=title, href=href)
            yield item_obj

        # 拿分页
        # page_list = Selector(response=response).xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        # for page in page_list:
        #     url = "http://dig.chouti.com" + page
        #     # 把分页的URL发到后端,再次进行获取
        #     yield Request(url=url)
        #     # yield Request(url=url,callback=self.func)  # default: callback=parse


# class ChouTiSpider(scrapy.Spider):
#     # 爬虫应用的名称，通过此名称启动爬虫命令
#     name = "chouti"
#     # 允许的域名
#     allowed_domains = ["chouti.com"]
#
#     cookie_dict = {}
#     has_request_set = {}
#
#     def start_requests(self):
#         url = 'http://dig.chouti.com/'
#         yield Request(url=url, callback=self.login)
#
#     def login(self, response):
#         cookie_jar = CookieJar()
#         cookie_jar.extract_cookies(response, response.request)
#         self.cookie_dict = cookie_jar
#
#         req = Request(
#             url='http://dig.chouti.com/login',
#             method='POST',
#             headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
#             body='phone=8613552791537&password=abc100200&oneMonth=1',
#             cookies=self.cookie_dict,
#             callback=self.check_login
#         )
#         yield req
#
#     def check_login(self, response):
#         req = Request(
#             url='http://dig.chouti.com/',
#             method='GET',
#             callback=self.show,
#             cookies=self.cookie_dict,
#             dont_filter=True
#         )
#         yield req
#
#     def show(self, response):
#         hxs = HtmlXPathSelector(response)
#         news_list = hxs.select('//div[@id="content-list"]/div[@class="item"]')
#         for new in news_list:
#             link_id = new.xpath('*/div[@class="part2"]/@share-linkid').extract_first()
#             yield Request(
#                 url='http://dig.chouti.com/link/vote?linksId=%s' % (link_id,),
#                 method='POST',
#                 cookies=self.cookie_dict,
#                 callback=self.do_favor
#             )
#
#         page_list = hxs.select('//div[@id="dig_lcpage"]//a[re:test(@href, "/all/hot/recent/\d+")]/@href').extract()
#         for page in page_list:
#             page_url = 'http://dig.chouti.com%s' % page
#             import hashlib
#             hash = hashlib.md5()
#             hash.update(bytes(page_url, encoding='utf-8'))
#             key = hash.hexdigest()
#             if key in self.has_request_set:
#                 pass
#             else:
#                 self.has_request_set[key] = page_url
#                 yield Request(
#                     url=page_url,
#                     method='GET',
#                     callback=self.show
#                 )
#
#     def do_favor(self, response):
#         print(response.text)