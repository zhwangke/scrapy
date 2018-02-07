# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    url = 'https://movie.douban.com/top250?start=0'
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        movie = response.xpath('//div[@class="item"]')
        for each in movie:
            item = DoubanItem()
            item['rank'] = each.xpath('./div/em/text()').extract()[0]
            item['name'] = each.xpath('./div/a/img/@alt').extract()[0]
            item['link'] = each.xpath('./div[@class="info"]/div/a/@href').extract()[0]
            item['grade'] = each.xpath('./div[@class="info"]/div/div/span/text()').extract()[0]

            tiem = each.xpath('./div[@class="info"]/div/p/text()').extract()[1]
            item['time'] = "".join(tiem).strip()

            comment = each.xpath('./div[@class="info"]/div/p/span/text()').extract()
            if len(comment) != 0:
                item['comment'] = comment[0]

            yield item

        if self.offset < 225:
            self.offset += 25

        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)