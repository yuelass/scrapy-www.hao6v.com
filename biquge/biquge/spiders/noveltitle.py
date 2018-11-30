import scrapy
from biquge.items import BiqugeItemTitle

class BiqugeSpider(scrapy.Spider):
	  




    name = 'novel-title'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/15/15043/']
    def parse(self, response):
      	  # 请求第一页
          yield scrapy.Request(response.url, callback=self.parse_next)
            
    def parse_next(self, response):
          novel = BiqugeItemTitle()
          novel['bookname']=response.xpath('//*[@id="info"]/h1/text()').extract()[0]
          novel['author']=response.xpath('//*[@id="info"]/p[1]/text()').extract()[0]
          novel['newtitle'] = response.xpath('//*[@id="info"]/p[4]/a/text()').extract()[0]
          novel['newtitleurl']= response.xpath('//*[@id="info"]/p[4]/a/@href').extract()[0]
          novel['newtitletime'] = response.xpath('//*[@id="info"]/p[3]/text()').extract()[0]
          yield novel
          for item in response.xpath('//*[@id="list"]/dl/dd'):
       	      novel = BiqugeItemTitle() 
              #print("-----")
              #print(item.xpath('span[1]/a/text()').extract()[0])
              novel['name']=item.xpath('a/text()').extract()[0]
              novel['nameurl']=item.xpath('a/@href').extract()[0]

              yield novel
