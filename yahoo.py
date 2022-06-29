from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import logging

def getYahooInfo(url):

    sth = logging.StreamHandler()
    flh = logging.FileHandler('./debug.log')
    logging.basicConfig(level=logging.INFO, handlers=[sth, flh])
    logger = logging.getLogger(__name__)

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome(executable_path=os.getcwd() + '/chromedriver', options=options)
    driver.get(url)
    
    shopName = driver.find_element(By.CSS_SELECTOR, 'div.mdBreadCrumb li:first-child span').text

    items = driver.find_elements(By.CSS_SELECTOR, 'div#itmlst>ul>li')
    
    yahooInfos = []
    for item in items:
        detailUrl = item.find_element(By.CSS_SELECTOR, 'div.elName>a').get_attribute('href')
        price = item.find_element(By.CSS_SELECTOR, 'span.elPriceValue').text
        price = price.replace(',', '')
        price = price.replace('円', '')
        yahooInfos.append({'shop':shopName, 'url':detailUrl, 'price':price})

    for yahooInfo in yahooInfos:
        try:
            driver.get(yahooInfo['url'])
            logger.info('ok')
        except Exception:
            pass
            logger.info('pass')

        detail = driver.find_element(By.CSS_SELECTOR, 'div#itm_cat')
        elRows = detail.find_elements(By.CSS_SELECTOR, 'li.elRow')

        yahooInfo['janCode'] = ''
        for elRow in elRows:
            title = elRow.find_element(By.CSS_SELECTOR, 'div.elRowTitle > p').text
            if title.startswith('JAN'):
                yahooInfo['janCode'] = elRow.find_element(By.CSS_SELECTOR, 'div.elRowData > p').text

        logger.info(yahooInfo)

    driver.quit()

    return yahooInfos
