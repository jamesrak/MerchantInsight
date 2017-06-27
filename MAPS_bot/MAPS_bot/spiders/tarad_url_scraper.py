# coding=utf-8
import scrapy
import re

class Tarad_url_scraper(scrapy.Spider):
   name = "Tarad_url_scraper"
   start_urls = [
       'https://www.tarad.com/category/1771/',
       'https://www.tarad.com/category/2641/',
       'https://www.tarad.com/category/4190/',
       'https://www.tarad.com/category/4366/',
       'https://www.tarad.com/category/807/',
       'https://www.tarad.com/category/3323/',
       'https://www.tarad.com/category/4476/',
       'https://www.tarad.com/category/3587/',
       'https://www.tarad.com/category/597/',
       'https://www.tarad.com/category/4260/',
       'https://www.tarad.com/category/3119/',
       'https://www.tarad.com/category/4815/',
       'https://www.tarad.com/category/4732/',
       'https://www.tarad.com/category/5045/',
       'https://www.tarad.com/category/1/',
       'https://www.tarad.com/category/3983/',
       'https://www.tarad.com/category/5619/',
       'https://www.tarad.com/category/3726/',
       'https://www.tarad.com/category/2132/',
       'https://www.tarad.com/category/5104/',
       'https://www.tarad.com/category/2114/',
       'https://www.tarad.com/category/5461/',
       'https://www.tarad.com/category/5536/',
       'https://www.tarad.com/category/5653/']

   def parse(self, response):

       for url in response.xpath("//div[@class='n_merchant']/a/@href").extract():
           yield {
               'shop_url': url
           }

       current_start_url = response.request.url
       page_offset = 60
       active_page = response.xpath("//a[@class='active']/text()").extract_first()
       if int(active_page) > 1 :
           current_start_url = re.search(r'(.+)\?&per_page=', response.request.url).group(1)
       next_page = (int(active_page) * page_offset)
       next_page_url = current_start_url + "?&per_page=" + str(next_page)
       if next_page_url is not None:
           yield scrapy.Request(response.urljoin(next_page_url))

