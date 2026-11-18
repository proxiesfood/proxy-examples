# pip install scrapy (2.13 or newer), then: scrapy runspider ip.py
import scrapy


class IpSpider(scrapy.Spider):
    name = "ip"

    async def start(self):
        yield scrapy.Request("https://icanhazip.com", meta={"proxy": "http://USERNAME:PASSWORD@proxies.proxiesfood.com:81"})

    def parse(self, response):
        print(response.text)
