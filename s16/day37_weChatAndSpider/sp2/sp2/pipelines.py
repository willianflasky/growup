# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class Sp2Pipeline(object):
    def process_item(self, item, spider):
        # item 就是yield过来的数据对象
        # spider 就是chouti爬虫对象
        print(item, spider)
        return item
        # if spider.name == 'chouti':
            # raise DropItem()  # 后面的pipeline就不再执行了

