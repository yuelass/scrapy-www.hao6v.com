# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name  = scrapy.Field()
    nameurl = scrapy.Field()
    newtitle = scrapy.Field()
    newtitleurl = scrapy.Field()


class BiqugeItemTitle(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    bookname = scrapy.Field()
    name  = scrapy.Field()
    nameurl = scrapy.Field()
    author = scrapy.Field()
    newtitle  = scrapy.Field()
    newtitleurl = scrapy.Field()
    newtitletime = scrapy.Field()

class BiqugeItemText(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title  = scrapy.Field()
    text = scrapy.Field()

class FictionItem(scrapy.Item): 
    name = scrapy.Field()   #小说名字  
    chapter_name = scrapy.Field()   #小说章节名字  
    chapter_content = scrapy.Field()    #小说章节内容   
