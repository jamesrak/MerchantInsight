import json

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/Plazathai_url.json') as json_data:
    plaza = json.load(json_data)

url = set()
data = []

for item in plaza:
    # print("collect : " + item['shop_url'])
    if (item['shop_url'] == 'http://www.plazathai.com/board/index.php?topic=21.0'):
        continue
    url.add(item['shop_url'])

print("url unique number = " + str(len(url)))

for url in list(url):
    data.append({'shop_url' : url})

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/Plazathai_url_unique.json', 'w') as json_data:
    json.dump(data, json_data)