# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZuFangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    zuFangType = scrapy.Field()
    fangJianType = scrapy.Field()
    size = scrapy.Field()
    chaoXiang = scrapy.Field()
    area1=scrapy.Field()
    area2 = scrapy.Field()
    area3 = scrapy.Field()
    jiaoTongJuLi = scrapy.Field()
    liangDian = scrapy.Field()
    price = scrapy.Field()

