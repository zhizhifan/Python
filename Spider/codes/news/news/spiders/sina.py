import scrapy


class SinaSpider(scrapy.Spider):
    name = "sina"
    allowed_domains = ["news.sina.com.cn"]
    start_urls = ["https://news.sina.com.cn"]

    def parse(self, response):
        pass
