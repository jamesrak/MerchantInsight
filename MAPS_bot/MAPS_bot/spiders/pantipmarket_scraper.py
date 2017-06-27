# -*- coding: utf-8 -*-
import scrapy
import re

class Pantipmarket_scraper(scrapy.Spider):
    name = 'Pantipmarket_scraper'
    start_urls = [
        'https://www.pantipmarket.com/mall/center/index.php?node=directory',
    ]

    def parse(self, response):
        for phone_list in response.xpath("//div[@class='t_contact_mobile']").extract():
            phone_list = phone_list.replace("-", "")
            try:
                phone_number = re.search(r'\d\d\d\d\d\d\d\d\d\d', phone_list, re.M|re.I).group()
                yield {
                    'phone_number' : phone_number
                }
            except Exception:
                print("Something's wrong!")

        page_offset = 50
        active_page = response.xpath("//a[@style='background-color:#E7FAFF;']/b/span/text()").extract_first()
        next_page = ((int(active_page)+1) * page_offset) - 50
        next_page_url = "https://www.pantipmarket.com/mall/center/index.php?node=directory&order=activateShop&b=" + str(next_page)
        print(next_page_url)
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
