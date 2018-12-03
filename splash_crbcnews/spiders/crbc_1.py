# -*- coding: utf-8 -*-
import scrapy                                                        
from scrapy_splash import SplashRequest

class CrbcSpider(scrapy.Spider):
    name = 'crbc_1'
    allowed_domains = ['cbrc.gov.cn']
    start_urls = ['http://www.cbrc.gov.cn/chinese/newListDoc/111002/1.html']

    #渲染入口页面
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, args={'images':0, 'timeout':3})
    
    #获取新闻列表页面的解析函数
    def parse(self, response):
        #获取新闻标题
        for sel in response.xpath('/html/body/center/div/div/div/table/tbody/tr[not(@valign)][position()>=2]'):
            newstitle = sel.xpath('./td/a/text()').extract_first()
            if newstitle:
                yield{'newstitle':newstitle,}
        
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
        pass
