import scrapy
from scrapytutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        pass
        quotes = response.css('.quote')
        #! 结果返回的是一个列表，存储了每个符合条件的Selector对象。

        for quote in quotes:
            item = QuoteItem()
            item['text'] = quote.css('.text::text').extract_first()
            #! 利用::text获取正文，不包含标签等其他信息，但仍然是Selector对象。
            #! 用extract()方法进一步提取Selector对象中的内容

            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item
        
        page_next = response.css('.pager .next a::attr("href")').extract_first()
        #!与前面::text获取正文不同，这里使用::attr()获取属性，括号里为具体的属性名
        
        url = response.urljoin(page_next)
        yield scrapy.Request(url=url, callback=self.parse)
        #! callback回调，仍用相同的parse方法


