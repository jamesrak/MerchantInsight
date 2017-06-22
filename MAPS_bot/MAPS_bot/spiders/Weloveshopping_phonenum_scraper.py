import scrapy
import json
import re

class Weloveshopping_phonenum_scraper(scrapy.Spider):
   name = "Weloveshopping_phonenum_scraper"
   start_urls = []
   loaded_urls = []

   # Load url data from json
   ## Format [
   ## {"url": "https://store.weloveshopping.com/beigerabbit44/info"},
   ## {"url": "https://store.weloveshopping.com/tharich"},
   # ]


   try:
       with open('Weloveshopping_url.json') as json_data:
           loaded_urls = json.load(json_data)
   except (OSError, IOError):
       print("Get an exception!")

   # Get info url ( every shops have same info format )
   for url in loaded_urls:
       start_urls.append(url['url'] + '/info')

   def parse(self, response):

       # Example data from shop's info page
       ## [
       ##     '<div class="col-lg-11 col-sm12">2/230 คอนโดศุภาลัยปาร์คแยกเกษตร ถนนประเสริญมนูกิจ แขวงเสนานิคม เขตจตุจักร 10900 เสนานิคม จตุจักร กรุงเทพมหานคร 10900</div>',
       ##     '<div class="col-lg-11 col-sm12"> 0617145577 </div>',
       ##     '<div class="col-lg-11 col-sm12">beigerabbit44@gmail.com</div>',
       ##     '<div class="col-lg-11 col-sm12">https://store.weloveshopping.com/beigerabbit44</div>'
       ## ]

       for text in response.xpath("//div[@class='col-lg-11 col-sm12']/text()").extract():

            # Change Format 061-714-5577 to 0617145577
            text = text.replace("-", "")
            phone_number = re.search(r'\d\d\d\d\d\d\d\d\d\d', text, re.M|re.I)
            if (phone_number is not None):
                phone_number = phone_number.group()
                yield {
                    'phone_number' : phone_number
                }

