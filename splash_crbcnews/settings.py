# -*- coding: utf-8 -*-

# Scrapy settings for splash_crbcnews project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'splash_crbcnews'

SPIDER_MODULES = ['splash_crbcnews.spiders']
NEWSPIDER_MODULE = 'splash_crbcnews.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'splash_crbcnews (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
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
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'splash_crbcnews.middlewares.SplashCrbcnewsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'splash_crbcnews.middlewares.SplashCrbcnewsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'splash_crbcnews.pipelines.SplashCrbcnewsPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


#Splash 服务器地址
SPLASH_URL = 'http://localhost:8050'

#开启Splash的两个下载中间件并调整HttpCompressionMiddleware的次序
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware':723,
    'scrapy_splash.SplashMiddleware':725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware':810,
}

#设置去重过滤器
#DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'

#用来支持cache_args（可选）
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware':100,
}

#指定爬虫所使用的Redis数据库
REDIS_URL = 'redis://127.0.0.1:6379'

#使用scrapy_redis的调度器替代Scrapy原版调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

#使用scrapy_redis的REPDuperFilter作为去重过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

#启用scrapy_redis的RedisPipeline将爬取到的数据汇总到Redis数据库
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline':300,
}

#爬虫停止后，保留/清理Redis中的请求队列以及去重集合
#True：保留，False：清理，默认为False
SCHEDULER_PERSIST = True
