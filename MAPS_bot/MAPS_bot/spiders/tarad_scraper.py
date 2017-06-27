import scrapy
import json
import re

class Tarad_scraper(scrapy.Spider):
   name = "Tarad_scraper"
   start_urls = []
   loaded_urls = []

   try:
       with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/Tarad_url.json') as json_data:
           loaded_urls = json.load(json_data)
   except (OSError, IOError):
       print("Get an exception!")

   for url in loaded_urls:
       start_urls.append(url['shop_url'] + "/payment")
   start_urls = list(set(start_urls))

   def parse(self, response):
       text = response.xpath("//td").re(r'transfer_kb.+')[0]
       # Change Format 061-714-5577 to 0617145577
       text = text.replace("-", "")
       account = re.search(r'\d\d\d\d\d\d\d\d\d\d', text, re.M|re.I)
       if (account is not None):
           account = account.group()
           yield {
               'account' : account
           }