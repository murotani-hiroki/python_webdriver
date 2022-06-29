from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import logging

def getAmazonInfo(janCode):

    sth = logging.StreamHandler()
    flh = logging.FileHandler('./debug.log')
    logging.basicConfig(level=logging.INFO, handlers=[sth, flh])
    logger = logging.getLogger(__name__)

    if not janCode:
        return {'asin':'', 'price':''}

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path=os.getcwd() + '/chromedriver', options=options)
    driver.get('https://www.amazon.co.jp')
    input = driver.find_element(By.NAME, 'field-keywords')
    input.send_keys(janCode)
    input.submit()

    try: 
        item = driver.find_element(By.CSS_SELECTOR, 'div.s-asin')
        if not item:
            driver.quit()
            return {'asin':'', 'price':''}
    except Exception:
        logger.info('div.s-asin not found.')
        return {'asin':'', 'price':''}
    asin = item.get_attribute('data-asin')

    price = ''
    item = driver.find_element(By.CSS_SELECTOR, 'div.s-result-item div.sg-col-inner .a-price-whole')
    if item:
        price = item.text
        price = price.replace('¥', '')
        price = price.replace('￥', '')
        price = price.replace(',', '')

    driver.quit()

    asin = {'asin':asin, 'price':price} 
    logger.info(asin)

    return asin 