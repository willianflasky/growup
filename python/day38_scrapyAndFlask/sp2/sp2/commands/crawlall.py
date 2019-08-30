from scrapy.commands import ScrapyCommand
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
from scrapy.crawler import Crawler
class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        # scrapy.crawler.CrawlerProcess.crawl
        #       scrapy.crawler.Crawler.crawl # 执行代码
        # scrapy.crawler.CrawlerProcess.start
        self.crawler_process.crawl('chouti', **opts.__dict__)
        self.crawler_process.start()

        # spider_list = self.crawler_process.spiders.list()
        # for name in spider_list:
        #     self.crawler_process.crawl(name, **opts.__dict__)
        # self.crawler_process.start()