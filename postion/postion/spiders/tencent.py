# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from postion.items import PostionItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    rules = (
        Rule(LinkExtractor(allow='start=\d+')),
        Rule(LinkExtractor(allow='id=\d+'),callback='parse_item',follow=False)
    )

    def parse_item(self, response):
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        item = PostionItem()
        list = response.xpath('//ul/li/text()').extract()[:-2]
        details = " ".join(list)
        item['details'] = details

        yield item