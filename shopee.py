from itertools import product
from webbrowser import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
from time import sleep
import time
import json

def get_price(soup):
    tag = ""
    value = ""
    try:
        tag = soup.select_one('div.pmmxKx')
        value = tag.text.split("-")[0].strip()
    except Exception as e:
        print("get_price() Error: " + str(e))

    return {"source": str(tag), "value": value}

def get_currency(soup):
    tag = ""
    value = ""
    try:
        tag = soup.select_one('div.pmmxKx')
        value = tag.text.split("-")[0].strip()[0]
    except Exception as e:
        print("get_currency() Error: " + str(e))

    return {"source": str(tag), "value": value}

def get_stock(soup):
    tag = ""
    values = {}
    try:
        tag = soup.select('div._3Xk7SJ')

        for label in tag:
            label_title = label.select_one('label.UWd0h4').text
            if label_title in ["Stock", "Discount Stock", "Other stocks"]:
                stock_value = label.select_one('div').text
                values[label_title] = stock_value

    except Exception as e:
        print("get_stock() Error:" + str(e))
    
    return {"source": str(tag), "value": values}

def get_description(soup):
    tag = ""
    value = ""
    try:
        tag = soup.select_one('p.hrQhmh')
        value = tag.text

    except Exception as e:
        print("get_description() Error:" + str(e))

    return {"source": str(tag), "value": value}

def get_specifications(soup):
    tag = ""
    values = {}

    try:
        tag = soup.select('div._3Xk7SJ')

        for label in tag:
            label_title = label.select_one('label.UWd0h4').text
            if label_title not in ["Stock", "Discount Stock", "Other stocks", "Brand"]:
                if label_title == "Category":
                    value = label.select('div > a')[-1]
                else:
                    value = label.select_one('div')

                values[label_title] = value.text
    except Exception as e:
        print("get_specifications() Error:" + str(e))
    
    return {"source": str(tag), "value": values}

def get_brand(soup):
    tag = ""
    value = ""
    brand_found = False

    try:
        tag = soup.select('div._3Xk7SJ')

        for label in tag:
            label_title = label.select_one('label.UWd0h4').text
            if label_title == "Brand":
                brand_found = True
                value = label.select_one('a').text.strip()
        
        if not brand_found: tag = ""

    except Exception as e:
        print("get_specifications() Error:" + str(e))
    
    return {"source": str(tag), "value": value}

def get_vid_urls(soup):
    tags = ""
    value = []
    has_src = False

    try:
        tags = soup.select('video')

        if tags:
            for videos in tags:
                if videos.has_attr('src'):
                    value.append(videos['src'])
                    has_src = True

        if not has_src: tags = ""

    except Exception as e:
        print("get_vid_urls() error: " + str(e))
    
    return {"source": str(tags), "value": value}

def get_imgs_urls():
    tags = ""
    value = []

    try:
        thumbnail = chrome_driver.find_element(By.CLASS_NAME, 'xljt99')
        
        thumbnail_click = ActionChains(chrome_driver).click(thumbnail)
        thumbnail_click.perform()
        
        sleep(1)

        html = chrome_driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        new_soup = BeautifulSoup(html, "lxml")

        tags = new_soup.select('div.-EByYP > div.Mzs0kz > div._8akja2')
        for thumbnail in tags:
            style = thumbnail['style']
            background_image = style.split(';')[0]
            url = background_image.split(':')[2]
            value.append('https:' + url[:-5])

        # tags = soup.select('div.agPpyA._8akja2')

        # for thumbnail in tags:
        #     print(thumbnail)
        #     style = thumbnail['style']
        #     background_image = style.split(';')[0]
        #     url = background_image.split(':')[2]
        #     value.append('https:' + url[:-5])

    except Exception as e:
        print("get_video_urls() error: " + str(e))

    return {"source": str(tags), "value": value}

def get_delivery():
    tag = ""
    value = ""

    try:
        drawer = chrome_driver.find_element(By.CLASS_NAME, '_3AWhy3')
        
        hover_drawer = ActionChains(chrome_driver).move_to_element(drawer)
        hover_drawer.perform()
        
        sleep(1.5)

        html = chrome_driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        new_soup = BeautifulSoup(html, "lxml")

        tag = new_soup.select_one('div._1XIpMC')
        value = tag.text

    except Exception as e:
        print('get_delivery() error: ' + str(e))

    return {'source': str(tag), 'value': value}

def get_shipping():
    tag = ""
    value = ""

    try:
        drawer = chrome_driver.find_element(By.CLASS_NAME, '_3AWhy3')
        
        hover_drawer = ActionChains(chrome_driver).move_to_element(drawer)
        hover_drawer.perform()
        
        sleep(1.5)

        html = chrome_driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        new_soup = BeautifulSoup(html, "lxml")

        tag = new_soup.select_one('div.tKRqjN')
        value = tag.text

    except Exception as e:
        print('get_shipping() error: ' + str(e))

    return {'source': str(tag), 'value': value}

if __name__ == "__main__":
    url = str(input("Product URL: "))

    start_time = time.time()
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    chrome_driver.get(url)
    delay_in_seconds = 5

    try:
        WebDriverWait(chrome_driver, delay_in_seconds)
        html = chrome_driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
        soup = BeautifulSoup(html, "lxml")

        data = {}

        data['price'] = get_price(soup)
        data['currency'] = get_currency(soup)
        data['stock'] = get_stock(soup)
        data['description'] = get_description(soup)
        data['specifications'] = get_specifications(soup)
        data['brand'] = get_brand(soup)
        data['delivery'] = get_delivery()
        data['shipping'] = get_shipping()
        data['img_urls'] = get_imgs_urls()
        data['vid_urls'] = get_vid_urls(soup)

        with open('shopee_scrape_result.json', 'w', encoding="utf8") as json_file:
            result = json.dumps(data, indent=4, ensure_ascii=False)
            json_file.write(result)

        chrome_driver.quit()
    except TimeoutException:
        print("Timeout!")
    
    end_time = time.time()

    exec_time = end_time - start_time

    print(exec_time)
    

        