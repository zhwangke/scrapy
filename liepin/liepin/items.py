# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LiepinItem(scrapy.Item):
    # define the fields for your item here like:

    position = scrapy.Field()
    welfare = scrapy.Field()
    annual = scrapy.Field()
    worklocation = scrapy.Field()
    education = scrapy.Field()
    expreience = scrapy.Field()
    condition = scrapy.Field()
    company = scrapy.Field()
    companylocation = scrapy.Field()
    type = scrapy.Field()
    scale = scrapy.Field()



