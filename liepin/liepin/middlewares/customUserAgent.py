# -*- coding:utf-8 -*-

from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from liepin.middlewares.resource import USER_AGENT_LIST
import random

class RandomUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        list = random.choice(USER_AGENT_LIST)
        request.headers.setdefault('User-Agent', list)