from scrapy import signals


class MyExtension(object):
    def __init__(self):
        pass

    @classmethod
    def from_crawler(cls, crawler):
        obj = cls()

        crawler.signals.connect(obj.xxxxxx, signal=signals.engine_started)
        crawler.signals.connect(obj.rrrrr, signal=signals.spider_closed)

        return obj

    def xxxxxx(self, spider):
        print('open')

    def rrrrr(self, spider):
        print('open')