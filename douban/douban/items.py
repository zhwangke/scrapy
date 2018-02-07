# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影排名
    rank = scrapy.Field()
    #电影名字
    name = scrapy.Field()
    #详情链接
    link = scrapy.Field()
    #导演 上映时间
    time = scrapy.Field()
    #评分
    grade = scrapy.Field()
    #电影简评
    comment = scrapy.Field()