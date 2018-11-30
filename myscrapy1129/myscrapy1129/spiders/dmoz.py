# -*- coding: utf-8 -*-
import scrapy
from myscrapy1129.items import Myscrapy1129Item

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        "https://www.kuaidaili.com/free/inha/1/",
        "https://www.kuaidaili.com/free/inha/2/",
        #"https://www.kuaidaili.com/free/inha/3/",
        #"https://www.kuaidaili.com/free/inha/4/",
        #"https://www.kuaidaili.com/free/inha/5/",
        #"https://www.kuaidaili.com/free/inha/6/",
    ]
# //*[@id="listnav"]/ul/li[9]/a/text() //*[@id="list"] //*[@id="list"]/table/tbody/tr[1]/td[1] //*[@id="list"]/table/tbody/tr[1] //*[@id="list"]/table/tbody
    def parse(self, response):
        #sel=response.xpath('//*[@id="list"]')
        #dl1 = response.xpath('//*[@id="list"]/table/tbody')
        trs=response.xpath('//*[@id="list"]/table/tbody/tr')
        #print(dl)
        for tr_selector in trs:
            item = Myscrapy1129Item()
            item['ip'] = tr_selector.xpath('''./td[1]/text()''').extract_first()
            item['port'] = tr_selector.xpath('''./td[2]/text()''').extract_first()
            item['anonymity'] = tr_selector.xpath('''./td[3]/text()''').extract_first()
            item['types'] = tr_selector.xpath('''./td[4]/text()''').extract_first()
            item['location'] = tr_selector.xpath('''./td[6]/text()''').extract_first()
            yield item