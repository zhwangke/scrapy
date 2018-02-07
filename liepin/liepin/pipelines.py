# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class LiepinPipeline(object):
    def __init__(self):
        self.filename = codecs.open("liepin.json","w",encoding="utf-8")

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.filename.write(content)
        return item

    def colose_spider(self,spider):
        self.filename.close()