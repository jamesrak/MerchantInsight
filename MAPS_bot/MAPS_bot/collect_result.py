import json

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/out_data/lnwshop_out.json') as json_data:
    lnwshop = json.load(json_data)

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/out_data/pantipmarket_out.json') as json_data:
    pantip = json.load(json_data)

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/out_data/platinum_out.json') as json_data:
    platinum = json.load(json_data)

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/out_data/weloveshopping_out.json') as json_data:
    welove = json.load(json_data)

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/out_data/plazathai_out.json') as json_data:
    plazathai = json.load(json_data)

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/out_data/facebook_out.json') as json_data:
    facebook = json.load(json_data)


account_out = set()
phone_out = set()

for item in lnwshop:
    print("collect : " + item['account'])
    account_out.add(item['account'])

for item in pantip:
    print("collect : " + item['phone_number'])
    phone_out.add(item['phone_number'])

for item in plazathai:
    print("collect : " + item['phone_number'])
    phone_out.add(item['phone_number'])

for item in platinum:
    print("collect : " + item['phone_number'])
    phone_out.add(item['phone_number'])

for item in welove:
    print("collect : " + item['phone_number'])
    phone_out.add(item['phone_number'])

for item in facebook:
    print("collect : " + item['phone_number'])
    phone_out.add(item['phone_number'])

account_out = list(account_out)
phone_out = list(phone_out)

print("\naccount unique number = " + str(len(account_out)))
print("\nphone unique number = " + str(len(phone_out)))
print("\nTotal unique number = " + str(len(phone_out) + len(account_out)))