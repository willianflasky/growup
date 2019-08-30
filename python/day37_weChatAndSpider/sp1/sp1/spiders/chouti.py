# -*- coding: utf-8 -*-
import scrapy
import io,os,sys

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
from scrapy.selector import HtmlXPathSelector
from ..items import Sp1Item
from scrapy.http import Request

class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    # start_urls = ['http://dig.chouti.com/',]

    def start_requests(self):
        yield Request(url="http://dig.chouti.com/",headers={},callback=self.parse)

    def parse(self, response):
        # print(response.body)
        # print(response.text)
        hxs = HtmlXPathSelector(response)
        # result = hxs.select('//div[@id="yellow-msg-box-intohot"]')
        item_list = hxs.select('//div[@id="content-list"]/div[@class="item"]')
        for item in item_list:
            # item.select('./div[@class="news-content"]/div[@class="part2"]/text()').extract()
            # item.select('./div[@class="news-content"]/div[@class="part2"]/text()').extract_first()
            title = item.select('./div[@class="news-content"]/div[@class="part2"]/@share-title').extract_first()
            url = item.select('./div[@class="news-content"]/div[@class="part2"]/@share-pic').extract_first()
            # v = item.select('./div[@class="news-content"]/div[@class="part2"]/@share-title').extract_first()
            obj = Sp1Item(title=title,url=url)
            yield obj

        # 找到所有页码标签
        # hxs.select('//div[@id="dig_lcpage"]//a/@href').extract()
        page_url_list = hxs.select('//div[@id="dig_lcpage"]//a[re:test(@href,"/all/hot/recent/\d+")]/@href').extract()
        for url in page_url_list:
            url = "http://dig.chouti.com" + url
            obj = Request(url=url,callback=self.parse,headers={},cookies={})
            yield obj

