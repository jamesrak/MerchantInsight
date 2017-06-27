# -*- coding: utf-8 -*-
import scrapy
import re

class Weloveshopping_scraper(scrapy.Spider):
    name = 'Weloveshopping_url_scraper'
    start_urls = [
        'https://portal.weloveshopping.com/search?q=&f=shop:1&p=1',
    ]

    def parse(self, response):

        for url in response.xpath("//div[@class='shop-detail']/a/@href").extract():
            yield {
                'url' : url
            }

        active_page = response.xpath("//li[@class='active']/a/text()").extract_first()
        next_page = int(active_page) + 1
        next_page_url = "https://portal.weloveshopping.com/search?q=&f=shop:1&p=" + str(next_page)
        print(next_page_url)
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
