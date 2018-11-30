import scrapy
from biquge.items import BiqugeItem
from biquge.items import FictionItem

class BiqugeSpider(scrapy.Spider):
	  




    name = 'novel-book'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/fenlei/1_1.html']
    def parse(self, response):
      	  # 请求第一页
          yield scrapy.Request(response.url, callback=self.parse_next)
          
          # 请求其它页
          '''
          for page in response.xpath('///*[@id="pagelink"]/a'):
            link = page.xpath('@href').extract()[0]
            print(link)
            yield scrapy.Request(link, callback=self.parse_next)
          '''
          
          for page in range(2,190):
              link = 'http://www.xbiquge.la/fenlei/1_{}.html'.format(page)
              yield scrapy.Request(link, callback=self.parse_next)
          
    #获取网站玄幻类所有小说  
    def parse_next(self, response):
          for item in response.xpath('//*[@id="newscontent"]/div[1]/ul/li'):
       	      #novel = BiqugeItem() 
              #print("-----")
              #print(item.xpath('span[1]/a/text()').extract()[0])
              #novel['name']=item.xpath('span[1]/a/text()').extract()[0]
              #novel['nameurl']=item.xpath('span[1]/a/@href').extract()[0]
              #bookalltitle(item.xpath('span[1]/a/@href').extract()[0])
              #novel['newtitle']=item.xpath('span[2]/a/text()').extract()[0] 
              #novel['newtitleurl']=item.xpath('span[2]/a/@href').extract()[0]
              #书的名字
              #bookname = item.xpath('span[1]/a/text()').extract()[0]
              #bookurl = item.xpath('span[1]/a/@href').extract()[0]         
              #print('---')
              #print(bookname)
              #print(bookurl)
              #bookalltitle(bookurl)
              yield scrapy.Request(item.xpath('span[1]/a/@href').extract()[0],callback=self.bookalltitle)
    #获取该书所有的章节
    def bookalltitle(self,response):
          for item in response.xpath('//*[@id="list"]/dl/dd'):
              #章节名称
              #title = item.xpath('a/text()').extract()[0]
              titleurl = item.xpath('a/@href').extract()[0]
              #print('---')
              #print(title)
              #print(titleurl)
              titleurl  ="http://www.xbiquge.la"+titleurl
              yield scrapy.Request(titleurl,callback=self.bookalltext)

    #获取某章的内容
    def bookalltext(self,response):
          name =response.xpath('//*[@class="con_top"]/a[3]/text()').extract()[0]
          chapter_name=response.xpath('//*[@class="bookname"]/h1/text()').extract()[0]
          chapter_content = response.xpath('//*[@id="content"]/text()').extract()
          
          #print('-----')
          #print(name)
          #print(chapter_name)
          #print(chapter_content)
         
          item = FictionItem()  
          item['name'] = name  
          item['chapter_name'] = chapter_name  
          item['chapter_content'] = chapter_content  
          yield item 
     
           
     