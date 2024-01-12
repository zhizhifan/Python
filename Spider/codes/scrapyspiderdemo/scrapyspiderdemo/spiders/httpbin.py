from typing import Iterable
import scrapy
from scrapy.http import Request


# class HttpbinSpider(scrapy.Spider):
#     name = "httpbin"
#     allowed_domains = ["www.httpbin.org"]
#     start_urls = ["https://www.httpbin.org/get"]

    # def parse(self, response):
    #     print('url', response.url)
    #     print('status', response.status)
    #     print('request', response.request)
    #     print('headers', response.headers)
    #     print('text', response.text)

    # 这里并没有显示地声明初始请求，只是直接定义解析方法。这是因为Spider默认为我们实现了一个start_requests方法：
        
    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url=url, dont_filter=True)

    # 该方法生成了一个scrapy.http.Request实例。用这个Request类我们可以构造Request对象发送HTTP请求，它会被Engine交给Downloader进行处理执行。

    # 这里没有指定callback回调方法，其实就是默认parse方法，也可以这么写：callback=self.parse。
    
    # def parse(self, response):
    #     print('url', response.url)
    #     print('status', response.status)
    #     print('request', response.request)
    #     print('headers', response.headers)
    #     print('text', response.text)
        
    # 然后定义解析方法，于是每次都会对相应链接发送请并解析内容


    # 我们可以自己定义spider


# class HttpbinSpider(scrapy.Spider):
#     name = "httpbin"
#     allowed_domains = ["www.httpbin.org"]
#     start_url = "https://www.httpbin.org/get"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
#     }
#     cookies = {'name': 'germey', 'age': '26'}

#     def start_requests(self):
#         for offset in range(5):
#             url = self.start_url + f'?offset={offset}'
#             yield Request(url=url, headers=self.headers, cookies=self.cookies, meta={'offset':offset}, dont_filter=True, callback=self.parse_response)

#     def parse_response(self, response):
#         print('url', response.url)
#         print('status', response.status)
#         print('request', response.request)
#         print('headers', response.headers)
#         print('text', response.text)
#         print('meta', response.meta)


# 出了GET请求，还可以发送POST请求

import scrapy
# from scrapy.http import Request    GET请求
from scrapy.http import JsonRequest, FormRequest

class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_urls = ["https://www.httpbin.org/post"]
    data = {'name': 'germey', 'age': '26'}

    def start_requests(self):
        for url in self.start_urls:
            yield JsonRequest(url=url, data=self.data, callback=self.parse_response)

            yield FormRequest(url=url, formdata=self.data, callback=self.parse_response)

    def parse_response(self, response):
        print('text', response.text)
