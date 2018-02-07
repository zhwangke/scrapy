# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
class PositionSpider(scrapy.Spider):
    name = 'position'
    allowed_domains = ['tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            item = TencentItem()
            item['name'] = each.xpath('./td[1]/a/text()').extract()[0]
            item['link'] = each.xpath('./td[1]/a/@href').extract()[0]

            type = each.xpath('./td[2]/text()').extract()[0]
            if type != 0:
                item['type'] = type

            item['number'] = each.xpath('./td[3]/text()').extract()[0]
            item['location'] = each.xpath('./td[4]/text()').extract()[0]
            item['time'] = each.xpath('./td[5]/text()').extract()[0]

            yield item
        if self.offset < 6:
            self.offset += 10

        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)
