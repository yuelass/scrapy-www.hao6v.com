import scrapy
from biquge.items import BiqugeItemText

class BiqugeSpider(scrapy.Spider):
	  




    name = 'novel-text'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/15/15043/6812390.html']
    def parse(self, response):
      	  # 请求第一页
          yield scrapy.Request(response.url, callback=self.parse_next)

            
    def parse_next(self, response):
          novel = BiqugeItemText() 
          novel['title'] = response.xpath('//*[@id="wrapper"]/div[4]/div/div[2]/h1/text()').extract()
          novel['text']=response.xpath('//*[@id="content"]/text()').extract()
          yield novel
