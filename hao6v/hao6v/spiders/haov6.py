# -*- coding: utf-8 -*-
import scrapy
from hao6v.items import Hao6VItem

class Haov6Spider(scrapy.Spider):
    name = 'haov6'
    allowed_domains = ['hao6v.com']
    start_urls = ['http://www.hao6v.com/dy/index.html']
#//*[@id="main"]/div[2]/div[1]/ul/li[2]/a  //*[@id="main"]/div[2]/div[1] //*[@id="main"]/div[2]/div[1]/ul/li[1] //*[@id="main"]/div[2]/div[1]/ul/li[1]/span
    def parse(self,response):
        yield scrapy.Request(response.url, callback=self.parse_first)
        for page in range(2,265):
            link='http://www.hao6v.com/dy/index_{}.html'.format(page)
            yield scrapy.Request(link, callback=self.parse_first)
    def parse_first(self, d):
        items = []
        news=d.xpath('//*[@id="main"]/div[1]/div/ul/li')
        for new in news:
            item=Hao6VItem()
            item['url']=new.xpath('./a/@href').extract_first()
            items.append(item)

        for item in items:
            yield scrapy.Request(url=item['url'], callback=self.parse_second)
            #print(item['url'])
    def parse_second(self, response):
        item = Hao6VItem()
        #meta_1 = response.meta['meta_1']
        item['title'] = response.xpath('//*[@id="main"]/div[1]/div/h1/text()').extract_first()
        item['img']=response.xpath('//*[@id="endText"]/p[1]/img/@src').extract_first()
        item['downurl']=response.xpath('//*[@id="endText"]/table/tbody/tr[2]/td/a/@href').extract_first()
        print(item['downurl'])
        if item['downurl'] != None:
            yield item
#//*[@id="main"]/div[1]/div/ul/li[1]