import json
import re

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/facebook_api/facebook_all.json') as json_data:
    facebook_data = json.load(json_data)

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/facebook_api/facebook_all_v2.json') as json_data:
    facebook_data_2 = json.load(json_data)

phone_number_set = set()
phone_number_list = []
phone_number_set_2 = set()
phone_number_list_2 = []
all_phone_number_set = set()
target_category = ['Apparel & Clothing',
                   'Restaurant Supply Store',
                   'Bookstore',
                   'Commercial Equipment',
                   'Sushi Restaurant',
                   'Coffee Shop',
                   'Toy Store',
                   'Spa',
                   'Home Goods Store',
                   'Family Style Restaurant',
                   'Mattress Store',
                   'Beauty Salon',
                   'Hardware Store',
                   'Pub',
                   'Steakhouse',
                   'Electronics Store',
                   'Jewelry & Watches Store',
                   'Lighting Store',
                   'Local Business',
                   'Home Decor',
                   'Public Square / Plaza',
                   'Book',
                   'Jewelry Wholesaler',
                   'Jewelry/Watches',
                   'Product/Service',
                   'Thai Restaurant',
                   'Wholesale & Supply Store',
                   'Dessert Shop',
                   'Barbecue Restaurant',
                   'Maternity & Nursing Clothing Store',
                   'Costume Shop',
                   'Fast Food Restaurant',
                   'Mobile Phone Shop',
                   'Automotive Parts Store',
                   'Swimwear Store',
                   'Computer Store',
                   'American Restaurant',
                   'Cosmetics Store',
                   'Health/Beauty',
                   'Sunglasses & Eyewear Store',
                   'Tire Dealer & Repair Shop',
                   'Furniture Store',
                   'Outdoor Equipment Store',
                   'Middle Eastern Restaurant',
                   'Dance & Night Club',
                   'Japanese Restaurant',
                   'Bar',
                   'Music Store',
                   'Gift Shop',
                   'Accessories',
                   'Grocery Store',
                   'Seafood Restaurant',
                   'Tattoo & Piercing Shop',
                   'Local Service',
                   'Outlet Store',
                   'Car Wash',
                   'Tapas Bar & Restaurant',
                   'Party Supply & Rental Shop',
                   'Hair Salon',
                   'Sportswear Store',
                   'Cafe',
                   'Smoothie & Juice Bar',
                   'Food Wholesaler',
                   'Women\'s Clothing Store',
                   'Chinese Restaurant',
                   'Italian Restaurant',
                   'Camera Store',
                   'Pet Store',
                   'Beauty, Cosmetic & Personal Care',
                   'Blinds & Curtains Store',
                   'Arts & Crafts Store',
                   'Retail Company',
                   'Cafeteria',
                   'Mattress Wholesaler',
                   'Arts & Entertainment',
                   'Musical Instrument Store',
                   'Buffet Restaurant',
                   'Beauty/Cosmetics Company',
                   'Furniture',
                   'Ice Cream Shop',
                   'Shopping & Retail',
                   'Fruit & Vegetable Store',
                   'Health Spa',
                   'Halal Restaurant',
                   'Baby Goods/Kids Goods',
                   'Rental Shop',
                   'Nail Salon',
                   'Clothing Store',
                   'Automotive Wholesaler',
                   'Farmers Market',
                   'Moving Supply Store',
                   'Uniform Supplier',
                   'Book & Magazine Distributor',
                   'Automotive Dealership',
                   'Health Food Store',
                   'Sporting Goods Store',
                   'Sports & Recreation',
                   'Collectibles Store',
                   'Vegetarian/Vegan Restaurant',
                   'Sukiyaki Restaurant',
                   'Butcher Shop',
                   'Vitamins/Supplements',
                   'Latin American Restaurant',
                   'Medical Equipment Supplier',
                   'Flea Market',
                   'Market',
                   'Shopping Service',
                   'Medical Service',
                   'Car Stereo Store',
                   'Medical Center',
                   'Skin Care Service',
                   'Physical Therapist',
                   'Cultural Gifts Store',
                   'Automotive Store',
                   'Ramen Restaurant',
                   'Boutique Store',
                   'Pawn Shop',
                   'Home Theater Store',
                   'Restaurant',
                   'Bakery',
                   'Fashion',
                   'Wholesale Bakery',
                   'Beauty Supply Store',
                   'Seasonal Store',
                   'Pharmacy / Drugstore',
                   'Office Supplies',
                   'Automotive Customization Shop',
                   'Baby & Children\'s Clothing Store',
                   'Bags & Luggage Store',
                   'Bicycle Shop',
                   'Motorsports Store',
                   'Automotive Repair Shop',
                   'Restaurant Wholesaler',
                   'Beauty Store',
                   'Live & Raw Food Restaurant',
                   'Asian Restaurant',
                   'Spanish Restaurant',
                   'Footwear Store',
                   'Barber Shop',
                   'Automotive Body Shop',
                   'Health Food Restaurant',
                   'Vietnamese Restaurant',
                   'Carpet & Flooring Store',
                   'Men\'s Clothing Store',
                   'Bar & Grill',
                   'Bags/Luggage',
                   'Lifestyle Service',
                   'Car Dealership']

for data in facebook_data:
    try:
        phone_number = data['phone']
    except Exception:
        # print("Something wrong!")
        pass
    else:
        phone_number_set.add(phone_number)
        phone_number_list.append(phone_number)
        all_phone_number_set.add(phone_number)

for data in facebook_data_2:
    try:
        category = data['category']
        phone_number = data['phone']
    except Exception:
        # print("Something wrong!")
        pass
    else:
        if category in target_category:
            phone_number_set_2.add(phone_number)
            phone_number_list_2.append(phone_number)
            all_phone_number_set.add(phone_number)

print("\nTotal phone number : " + str(len(phone_number_list)))
print("\nTotal unique phone number : " + str(len(list(phone_number_set))))
print("\n\t##############################")
print("\nTotal V.2 phone number : " + str(len(phone_number_list_2)))
print("\nTotal V.2 unique phone number : " + str(len(list(phone_number_set_2))))
print("\nTarget categories : " + str(len(target_category)))
print("\n\t##############################")
print("\nAll unique phone number : " + str(len(list(all_phone_number_set))))

all_mobile_number_list = []
mobile_phone_prefix = ['01', '06', '08', '09']
for phone_number in list(all_phone_number_set):
    phone_number = phone_number.replace("+66", "0")
    phone_number = ''.join([s for s in phone_number if s.isdigit()])
    try:
        phone_number = re.search(r'[08|09|06|01]\d\d\d\d\d\d\d\d\d', phone_number, re.M|re.I).group()
    except Exception:
        pass
    else:
        print(phone_number)
        all_mobile_number_list.append(phone_number)

print("\n\t##############################")
print("\nAll unique mobile number : " + str(len(all_mobile_number_list)))

dump_data = []
for mobile_number in all_mobile_number_list:
    dump_data.append({'phone_number' : mobile_number})

with open('/Users/AUM/Desktop/MerchantInsight/MAPS_bot/MAPS_bot/facebook_api/facebook_out.json', 'w') as json_data:
    json.dump(dump_data, json_data)
