# -*- coding: utf-8 -*-

# Scrapy settings for sp2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sp2'

SPIDER_MODULES = ['sp2.spiders']
NEWSPIDER_MODULE = 'sp2.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sp2 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sp2.middlewares.Sp2SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    # 'sp2.middlewares.MyCustomDownloaderMiddleware': 543,
#    # 'sp2.download_middlewares.DownMiddleware1': 543,
#    # 'sp2.download_middlewares.DownMiddleware2': 544,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'sp2.extend.MyExtension': 500,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# from scrapy_redis.pipelines import RedisPipeline
# ITEM_PIPELINES = {
#    'scrapy_redis.pipelines.RedisPipeline': 300,
#    'sp2.pipelines.DbPipeline': 400,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# DOWNLOADER_HTTPCLIENTFACTORY = "scrapy.core.downloader.webclient.ScrapyHTTPClientFactory"
# DOWNLOADER_CLIENTCONTEXTFACTORY = "scrapy.core.downloader.contextfactory.ScrapyClientContextFactory"
# DOWNLOADER_CLIENTCONTEXTFACTORY = "sp2.https.MySSLFactory"


# ############ 自定义 ############
# from scrapy.dupefilter import RFPDupeFilter
# DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'
# DUPEFILTER_CLASS = 'sp2.my_filter.MyDupeFilter'
from scrapy.core.scheduler import Scheduler
# SCHEDULER = 'scrapy.core.scheduler.Scheduler'

# XXXXXXX = "chouti.json"
# UUUUUUU = "chouti_dev.json"
# ENV = "debug"
# COMMANDS_MODULE = "sp2.commands"

# ################### scrapy-redis组件 ###################
# import redis
# pip3 install redis

REDIS_URL = 'redis://user:pass@hostname:9001'  # 连接URL（优先于以上配置）
# REDIS_PARAMS  = {}                                  # Redis连接参数             默认：REDIS_PARAMS = {'socket_timeout': 30,'socket_connect_timeout': 30,'retry_on_timeout': True,'encoding': REDIS_ENCODING,}）
# REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient' # 指定连接Redis的Python模块  默认：redis.StrictRedis
# REDIS_ENCODING = "utf-8"                            # redis编码类型             默认：'utf-8'

# 去重规则（redis中的set集合）
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'  # 默认使用优先级队列（默认），其他：PriorityQueue（有序集合），FifoQueue（列表）、LifoQueue（列表）
SCHEDULER_QUEUE_KEY = '%(spider)s:requests'  # 调度器中请求存放在redis中的key
SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"  # 对保存到redis中的数据进行序列化，默认使用pickle
SCHEDULER_PERSIST = True  # 是否在关闭时候保留原来的调度器和去重记录，True=保留，False=清空
SCHEDULER_FLUSH_ON_START = True  # 是否在开始之前清空 调度器和去重记录，True=清空，False=不清空
SCHEDULER_IDLE_BEFORE_CLOSE = 10  # 去调度器中获取数据时，如果为空，最多等待时间（最后没数据，未获取到）。
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'  # 去重规则，在redis中保存时对应的key








