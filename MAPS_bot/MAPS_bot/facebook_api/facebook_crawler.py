#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import facebook
import re
import time
import json
import io
import string

token = "secret_token"

graph = facebook.GraphAPI(access_token=token, version=2.7)
thai_char_2 = ['ก', 'ข', 'ฃ','ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ' ,'ฎ' ,'ฏ' ,'ฐ',
             'ฑ' ,'ฒ', 'ณ', 'ด', 'ต', 'ถ' ,'ท' ,'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ',
             'ม', 'ย', 'ร', 'ล', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
eng_char_2 = ['a', 'e', 'i', 'o', 'u']
thai_char = ['ร้านค้า', 'ร้าน']
eng_char = ['shop', 'store']
keywords = thai_char + eng_char
item_count = 0
phone_number_set = set()
category_set = set()
data_out = []

for keyword in keywords:
    search_url = "search?q={}&type=page&fields=name,phone,category"
    pages = graph.request(search_url.format(keyword))

    # First page
    pageList = pages['data']
    for page in pageList:
        print(page)
        for key, value in page.items():
            if key.encode('ascii', 'ignore') == 'phone':
                phone_number_set.add(value.encode('ascii', 'ignore'))
            if key.encode('ascii', 'ignore') == 'category':
                category_set.add(value.encode('ascii', 'ignore'))
        data_out.append(page)
        item_count += 1

    # Next page
    while True:
        try:
            next = pages['paging']['next']
        except Exception:
            print("Error occur! There's no next page.")
            break
        else:
            next = re.search(r'search.+', pages['paging']['next'], re.I | re.M).group()
            print("################################################")
            print(next)
            print("################################################")
            pages = graph.request(next)

            pageList = pages['data']
            for page in pageList:
                print(page)
                for key, value in page.items():
                    if key.encode('ascii', 'ignore') == 'phone':
                        phone_number_set.add(value.encode('ascii', 'ignore'))
                    if key.encode('ascii', 'ignore') == 'category':
                        category_set.add(value.encode('ascii', 'ignore'))
                data_out.append(page)
                item_count += 1
            time.sleep(0.1)

print("\n\nTotal item counts : " + str(item_count))
print("\n\nTotal phone number unique : " + str(len(list(phone_number_set))))
print("\n\nTotal category unique : " + str(len(list(category_set))))

with io.open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/facebook_api/facebook_all_v3.json', 'w', encoding='utf8') as json_data:
    data = json.dumps(data_out, ensure_ascii=False)
    json_data.write(unicode(data))

