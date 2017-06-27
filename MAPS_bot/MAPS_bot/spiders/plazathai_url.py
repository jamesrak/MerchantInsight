# -*- coding: utf-8 -*-
import scrapy
import re


class Plazathai_url_scraper(scrapy.Spider):
    name = 'Plazathai_url_scraper'
    url_categories = [
        '/car-19',
        '/computer-5',
        '/mobile-17',
        '/camera-1',
        '/fashion-16',
        '/beauty-21',
        '/mom-18',
        '/home-23',
        '/decor-15',
        '/electronic-6',
        '/pet-9',
        '/collect-8',
        '/tour-11',
        '/sport-3',
        '/game-4',
        '/entertain-14',
        '/book-22',
        '/industry-25',
        '/business-12',
        '/art-20',
        '/food-24',
        '/office-26',
        '/other-27',
        '/education-2',
        '/music-7',
        '/ticket-10',
        '/clock-13',
]

    start_urls = []
    for category in url_categories:
        start_urls.append("http://www.plazathai.com" + category)

    print(start_urls)

    def parse(self, response):
        for url in response.xpath("//div[@class='listmR2']/a[@target='_blank']/@href").extract():
            yield {
                'shop_url': url
            }

        current_start_url = response.request.url
        active_page = response.xpath("//span[@class='numpage2']/text()").extract()[0]
        if int(active_page) > 1:
            current_start_url = re.search(r'(.+)-\d+', response.request.url).group(1)
        next_page = int(active_page) + 1
        next_page_url = current_start_url + "-" + str(next_page)
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
