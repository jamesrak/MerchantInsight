import scrapy
import json
import re

class Lnwshop_account_scraper(scrapy.Spider):
   name = "Lnwshop_account_scraper"
   start_urls = []
   loaded_urls = []

   # Load url data from json
   ## Format [
   # {"shop_url": ["http://888bike.net/"]},
   # {"shop_url": ["http://www.tookjingjing.com/"]},
   # ]

   try:
       with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/lnwshop_url.json') as json_data:
           loaded_urls = json.load(json_data)
   except (OSError, IOError):
       print("Get an exception!")

   # Get how2order url ( every shops have same how2order format )
   for url in loaded_urls:
       start_urls.append(url['shop_url'][0] + 'how2order')

   def parse(self, response):

       # Get body html from start_url by regex
       ## <div class="style_bank bank_kbank"><b>ธ.กสิกรไทย</b></div>
       ## <div class="style_number"><b>789-2-17330-8</b></div>
       text = response.xpath('//body').re(r'>ธ.กสิกรไทย.+\n.+')[0]

       # Change Format 789-2-17330-8 to 7892173308
       text = text.replace("-", "")
       account_number = re.search(r'\d\d\d\d\d\d\d\d\d\d', text, re.M|re.I).group()

       yield {
           'account' : account_number
       }

