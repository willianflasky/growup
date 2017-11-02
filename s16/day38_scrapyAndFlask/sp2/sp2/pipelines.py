# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class Sp2Pipeline(object):
    def __init__(self, file_path,env):
        self.file_path = file_path
        self.env = env

        self.file_obj = None

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        val = crawler.settings.get('XXXXXXX')
        env = crawler.settings.get('ENV')
        return cls(val,env)

    def process_item(self, item, spider):
        if spider.name == 'chouti':
            self.file_obj.write(item['url'])

        if self.env == 'debug':
            raise DropItem()
        else:
            return item

    def open_spider(self, spider):
        """
        爬虫开始执行时，只执行一次
        :param spider:
        :return:
        """
        self.file_obj = open(self.file_path, mode='a+')

    def close_spider(self, spider):
        """
        爬虫关闭时，只执行一次
        :param spider:
        :return:
        """
        self.file_obj.close()



class DbPipeline(object):
    def __init__(self, file_path):
        self.file_path = file_path

        self.file_obj = None

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        val = crawler.settings.get('UUUUUUU')
        return cls(val)

    def process_item(self, item, spider):
        if spider.name == 'chouti':
            self.file_obj.write(item['url'])
        return item

    def open_spider(self, spider):
        """
        爬虫开始执行时，只执行一次
        :param spider:
        :return:
        """
        self.file_obj = open(self.file_path, mode='a+')

    def close_spider(self, spider):
        """
        爬虫关闭时，只执行一次
        :param spider:
        :return:
        """
        self.file_obj.close()


