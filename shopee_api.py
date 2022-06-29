import requests
import json
import time
from datetime import datetime

def get_api_call(url):
    item_id = ""
    shop_id = ""

    url_parameters = url[8:].split('/')

    if len(url_parameters) == 2:
       url_parameters = url_parameters[1].split('?')[0].split('.')

    item_id = url_parameters[-1]
    shop_id = url_parameters[-2]

    data_call = f"https://shopee.ph/api/v4/item/get?itemid={item_id}&shopid={shop_id}"
    shipping_delivery_call = f'https://shopee.ph/api/v4/pdp/get_shipping?buyer_zipcode=&city=Metro%20Manila&district=&itemid={item_id}&shopid={shop_id}&state=Metro%20Manila&town='
    
    print(data_call + '\n' + shipping_delivery_call)

    return data_call, shipping_delivery_call

def get_price(data, url):
    value = ""

    try:
        price = str(data['price'])[:-5]
        value = f"{int(price):,}"

    except Exception as e:
        print("get_price() Error: " + str(e))

    return {'source': url, 'value': value}

def get_currency(data, url):
    value = ""
    try:
        pass
    except Exception as e:
        print("get_currency() Error: " + str(e))

    return {'source': url, 'value': value}

def get_stock(data, url):
    value = ""
    try:
        value = str(data['stock'])
    except Exception as e:
        print("get_stock() Error:" + str(e))
    
    return {'source': url, 'value': value}

def get_description(data, url):
    value = ""
    try:
        value = data['description']
    except Exception as e:
        print("get_description() Error:" + str(e))

    return {'source': url, 'value': value}

def get_specifications(data, url):
    value = {}

    try:
        if data['attributes']:
            for item in data['attributes']: 
                value['name'] = item['value']

    except Exception as e:
        print("get_specifications() Error:" + str(e))
    
    return {'source': url, 'value': value}

def get_brand(data, url):
    value = ""

    try:
        value = data['brand']
    except Exception as e:
        print("get_specifications() Error:" + str(e))
    
    return {'source': url, 'value': value}
    
def get_vid_urls(data, url):
    value = []
    url_to_pass = ""
    try:
        if data['video_info_list']:
            url_to_pass = url
            value = [item['default_format']['url'] for item in data['video_info_list']]
        
    except Exception as e:
        print("get_vid_urls() error: " + str(e))
    
    return {'source': url_to_pass, 'value': value}

def get_imgs_urls(data, url):
    value = []

    try:
        value = ['https://cf.shopee.ph/file/' + image for image in data['images']]

    except Exception as e:
        print("get_video_urls() error: " + str(e))

    return {'source': url, 'value': value}

def get_delivery(data, url):
    value = []    
    try:
        estimated_date_from = 0
        estimated_date_to = 0

        type = ''
        
        channel_info = []

        if data['ungrouped_channel_infos']:    
            type = 'ungrouped'
            channel_info = data['ungrouped_channel_infos']
        elif data['grouped_channel_infos_by_service_type']: 
            type = 'grouped'
            channel_info = data['grouped_channel_infos_by_service_type']

        for channel in channel_info:
            if type is 'grouped':
                for info in channel['channel_infos']:
                    print(info['name'])
                    estimated_date_from = info['channel_delivery_info']['estimated_delivery_date_from']
                    estimated_date_to = info['channel_delivery_info']['estimated_delivery_date_to']
            elif type is 'ungrouped':
                estimated_date_from = channel['channel_delivery_info']['estimated_delivery_date_from']
                estimated_date_to = channel['channel_delivery_info']['estimated_delivery_date_to']

        unformatted_date_from = datetime.fromtimestamp(estimated_date_from)
        unformatted_date_to = datetime.fromtimestamp(estimated_date_to)

        formatted_date_from = datetime.strftime(unformatted_date_from, '%b %d %Y')
        formatted_date_to = datetime.strftime(unformatted_date_to, '%b %d %Y')
        
        value = formatted_date_from + ' - ' + formatted_date_to
        
    except Exception as e:
        print('get_delivery() error: ' + str(e))

    return {'source': url, 'value': value}

def get_shipping(data, url):
    value = ""

    try:
        shipping_info = data['product_info']['shipping_fee_info']
        shipping_fee_min = str(shipping_info['min_price'])[:-5]
        value = f"{int(shipping_fee_min):,}"

    except Exception as e:
        print('get_shipping() error: ' + str(e))

    return {'source': url, 'value': value}

if __name__ == "__main__":
    url = str(input("Product URL: "))
    start_time = time.time()

    data_call, shipping_delivery_call = get_api_call(url)
    data_response = requests.get(data_call)
    shipping_delivery_response = requests.get(shipping_delivery_call)
    
    data = data_response.json()['data']
    shipping_delivery = shipping_delivery_response.json()['data']
    
    output = {}

    output['price'] = get_price(data, data_call)
    output['stock'] = get_stock(data, data_call)
    output['description'] = get_description(data, data_call)
    output['specifications'] = get_specifications(data, data_call)
    output['img_urls'] = get_imgs_urls(data, data_call)
    output['vid_urls'] = get_vid_urls(data, data_call)
    output['delivery'] = get_delivery(shipping_delivery, shipping_delivery_call)
    output['shipping'] = get_shipping(shipping_delivery, shipping_delivery_call)

    with open('shopee_scrape_result.json', 'w', encoding="utf8") as json_file:
        result = json.dumps(output, indent=4, ensure_ascii=False)
        json_file.write(result)
    
    end_time = time.time()
    exec_time = end_time - start_time
    print(exec_time)