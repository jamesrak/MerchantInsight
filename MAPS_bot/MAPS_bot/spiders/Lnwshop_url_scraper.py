# -*- coding: utf-8 -*-
import scrapy

class Lnwshop_url_scraper(scrapy.Spider):
    name = 'Lnwshop_url_scraper'
    start_urls = [
        'https://www.lnwshop.com/shop/all',
    ]

    def parse(self, response):
        for links in response.xpath('//div[@class="item_pin"]'):
            yield {
                'shop_url' : links.xpath("a/@href").extract()
            }

        next_page_url = response.xpath("//a[@class = 'tosakanth-action']").re(r'href="(.+)"><div')[1]
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
