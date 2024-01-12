from typing import Iterable
import scrapy
from scrapy.http import Request


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_urls = ["https://www.httpbin.org/get"]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, dont_filter=True)
    
    def parse(self, response):
        print('text', response.text)








