# -*- coding: utf-8 -*-
import scrapy
import re

class Platinum_scraper(scrapy.Spider):
    name = 'Platinum_scraper'
    start_urls = [
        'http://www.platinumfashionmall.com/directory/s=',
    ]

    def parse(self, response):
        for phone_list in response.xpath("//div[@class = 'tel light-grey size13 upcase']/text()").extract():
            phone_list = phone_list.replace("-", "")
            try:
                phone_number = re.search(r'\d\d\d\d\d\d\d\d\d\d', phone_list, re.M|re.I).group()
                yield {
                    'phone_number' : phone_number
                }
            except Exception:
                print("Something's wrong!")

        active_page = response.xpath("//a[@class = 'num active']/text()").extract_first()
        next_page = int(active_page) + 1
        next_page_url = "http://www.platinumfashionmall.com/directory/p-" + str(next_page) + "/"
        print(next_page_url)
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
