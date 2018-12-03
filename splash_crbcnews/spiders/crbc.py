# -*- coding: utf-8 -*-
import scrapy                                                        
from scrapy_splash import SplashRequest
from scrapy_redis.spiders import RedisSpider

#class CrbcSpider(scrapy.Spider):
class CrbcSpider(RedisSpider):
    name = 'crbc'
    allowed_domains = ['cbrc.gov.cn']
    #start_urls = ['http://www.cbrc.gov.cn/chinese/newListDoc/111002/1.html']

    #渲染入口页面
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, args={'images':0, 'timeout':3})
    
    #获取新闻列表页面的解析函数
    def parse(self, response):
        #获取新闻标题
        #for sel in response.xpath('/html/body/center/div/div/div/table/tbody/tr[not(@valign)][position()>=2]'):
        #    newstitle = sel.xpath('./td/a/text()').extract_first()
        #    if newstitle:
        #        yield{'newstitle':newstitle,}
        
        #获取新闻具体信息页面链接
        for le in response.xpath('/html/body/center/div/div/div/table/tbody/tr[not(@valign)][position()>=2]/td/a/@href').extract():
            if le:
                news_url = response.urljoin(le)
                #print("news_url is :" + news_url)
                yield SplashRequest(news_url, args={'images':0, 'timeout':3}, callback=self.parse_news)
        
        #获取下一页链接
        href = response.xpath('//a[./text()="下页"]//@href').extract_first()
        if href:
            url = response.urljoin(href)
            yield SplashRequest(url, args={'images':0, 'timeout':3})

    #获取新闻详细信息页面的解析函数
    def parse_news(self,response):
        title_x = response.xpath('//div[@class="Section0"]/p[contains(@style,"text-align:center")]//*/text()').extract()
        news_title = ""
        for x1 in title_x:
            news_title = news_title + x1
        
        context_x = response.xpath('//div[@class="Section0"]/*[contains(@style,"text-indent")]//span/text()').extract()
        news_context = ""
        for x2 in context_x:
            news_context = news_context + x2
        
        beizhu = response.xpath('normalize-space(//div[@id="docTitle"]/div/text())').extract_first()
        
        yield {'news_title':news_title, 'news_context':news_context, 'beizhu':beizhu}
