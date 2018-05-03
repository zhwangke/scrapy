# -*- coding: utf-8 -*-
import scrapy
from liepin.items import LiepinItem
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class PostionSpider(scrapy.Spider):
    name = 'postion'
    allowed_domains = ['liepin.com']
    url = 'https://www.liepin.com/zhaopin/?key=python&curPage='
    offset = 0
    start_urls = [url + str(offset)]
    """
    def parse(self,response):
        pattern = re.compile(r'https://www.liepin.com/job/\d+.shtml?')
        links = re.findall(pattern, response.body)
        for link in links:
            print link

        if self.offset < 20:
            self.offset += 1
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    """
    def parse(self,response):
        pattern = re.compile(r'https://www.liepin.com/job/\d+.shtml?')
        links = re.findall(pattern,response.body)
        for link in links:
            yield scrapy.Request(link,callback=self.parse_item)
        if self.offset < 99:
            self.offset += 1
        yield scrapy.Request(self.url + str(self.offset),callback=self.parse)

    def parse_item(self, response):
        item = LiepinItem()
        item['position'] = self.get_position(response)
        item['welfare'] = self.get_welfare(response)
        item['annual'] = self.get_annual(response)
        item['worklocation'] = self.get_worklocation(response)
        item['education'] = self.get_education(response)
        item['condition'] = self.get_condition(response)
        item['company'] = self.get_company(response)
        item['companylocation'] = self.get_companylocation(response)
        item['type'] = self.get_type(response)
        item['scale'] = self.get_scale(response)

        yield item
    def get_position(self,response):
        # 职位名字
        item['position'] = response.xpath('//h1/text()').extract()[0]

    def get_welfare(self, response):
        # 福利
        welfare = response.xpath('//div[@class="tag-list"]/span/text()').extract()
        item['welfare'] = "".join(welfare)

    def get_annual(self, response):
        # 年薪
        annual = response.xpath('//p[@class="job-item-title"]/text()').extract()[0]
        item['annual'] = annual.strip()

    def get_worklocation(self, response):
        # 工作地点
        worklocation = response.xpath('//div[@class="job-title-left"]/p/span/a/text()').extract()
        if len(worklocation) != 0:
            item['worklocation'] = worklocation[0]
        else:
            item['worklocation'] = response.xpath('//p[@class="basic-infor"]/span/text()').extract()[1].strip()

    def get_education(self, response):
        # 学历
        item['education'] = response.xpath('//div[@class="job-qualifications"]/span/text()').extract()[0]

    def get_expreience(self, response):
        # 工作经验
        item['expreience'] = response.xpath('//div[@class="job-qualifications"]/span/text()').extract()[1]

    def get_condition(self, response):
        # 职位描述
        condition = response.xpath('//div[@class="job-item main-message job-description"]/div/text()').extract()
        item['condition'] = "".join(condition).strip()

    def get_company(self, response):
        # 公司名字
        item['company'] = response.xpath('//h3/a/text()').extract()[0]

    def get_companylocation(self, response):
        # 公司地点
        companylocation = response.xpath('//ul[@class="new-compintro"]/li/text()').extract()[-1]
        item['companylocation'] = companylocation.split("：")[-1]

    def get_type(self, response):
        # 公司行业
        type = response.xpath('//ul[@class="new-compintro"]/li/a/text()').extract()
        if len(type) != 0:
            item['type'] = type[0]
        else:
            type = response.xpath('//ul[@class="new-compintro"]/li/text()').extract()[0]
            item['type'] = type.split("：")[-1]

    def get_scale(self, response):
        # 公司规模
        scale = response.xpath('//ul[@class="new-compintro"]/li/text()').extract()[-2]
        item['scale'] = scale.split("：")[-1]





