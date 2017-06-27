import scrapy
import json
import re

class Plazathai_scraper(scrapy.Spider):
   name = "Plazathai_scraper"
   start_urls = []
   loaded_urls = []

   try:
       with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/plazathai_url_unique.json') as json_data:
           loaded_urls = json.load(json_data)
   except (OSError, IOError):
       print("Get an exception!")

   for url in loaded_urls:
       start_urls.append(url['shop_url'] + "/contact_us/")

   def parse(self, response):
       # print(response.request.url)
       text = response.xpath("//body").extract()[0]
       text = re.search(r'มือถือ.+\n.+', text, re.M|re.I|re.U).group()
       # Change Format 061-714-5577 to 0617145577
       text = text.replace("-", "")
       phone_number = re.search(r'\d\d\d\d\d\d\d\d\d\d', text, re.M|re.I)
       if (phone_number is not None):
           phone_number = phone_number.group()
           yield {
               'phone_number' : phone_number
           }