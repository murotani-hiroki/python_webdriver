from yahoo import getYahooInfo
from amazon import getAmazonInfo
import logging

def getGoodsCsv(url): 

    sth = logging.StreamHandler()
    flh = logging.FileHandler('./debug.log')
    logging.basicConfig(level=logging.INFO, handlers=[sth, flh])
    logger = logging.getLogger(__name__)
    logger.info('--- getGoodsCsv start ---')

    yahooInfos= getYahooInfo(url)

    results = ['Yahoo JAN,Yahoo販売価格,ASIN,Amazon販売価格']
    for yahooInfo in yahooInfos:
        if not yahooInfo['janCode']:
            continue

        amazonInfo = getAmazonInfo(yahooInfo['janCode'])
        results.append(','.join([yahooInfo['janCode'], yahooInfo['price'], amazonInfo['asin'], amazonInfo['price']]))

    logger.info('--- getGoodsCsv end ---')
    return "\n".join(results)

if __name__ == '__main__':
    csv = getGoodsCsv('https://store.shopping.yahoo.co.jp/bestexcel/search.html')
    print(csv)