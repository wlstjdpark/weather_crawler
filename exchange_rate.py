# from https://github.com/skkong/CrawlingAPI/blob/master/getExchangeRate.py

import sys
import re
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request, urlopen
from urllib.parse import quote


def getPage(url):
    try:
        req = Request(url)
        res = urlopen(req)
        content = res.read()
    except:
        content = ""

    return content

def getExchangeOfNation(soup):
    dicExchange = {}
    alpha = '([A-Z]+)'

    for item in soup.table('tr')[2:]:
        nation = item('td')[0].text.strip()
        re_result = re.search(alpha, nation)
        nation = re_result.groups()[0]

        basicRateOfExchange = item('td')[1].text
        cash_buy = item('td')[2].text
        cash_sell = item('td')[3].text
        transfer_send = item('td')[4].text
        transfer_receive = item('td')[5].text

        dicExchange[nation] = {'basicRate':basicRateOfExchange, 'cashBuy':cash_buy, \
                   'cashSell':cash_sell, 'transferSend':transfer_send, 'transferReceive':transfer_receive}

    return dicExchange


url = "http://info.finance.naver.com/marketindex/exchangeList.nhn"
res = getPage(url)
soup = BeautifulSoup(res, 'html.parser')

nationExchangeRate = getExchangeOfNation(soup)


print(nationExchangeRate['USD'])
print(nationExchangeRate['JPY'])
print(nationExchangeRate['EUR'])
print(nationExchangeRate['CNY'])
print(nationExchangeRate['HKD'])

'''
미국 USD
유럽연합 EUR
일본 JPY
중국 CNY
홍콩 HKD
대만 TWD
영국 GBP
오만 OMR
캐나다 CAD
스위스 CHF
스웨덴 SEK
호주 AUD
뉴질랜드 NZD
체코 CZK
칠레 CLP
터키 TRY
몽골 MNT
이스라엘 ILS
덴마크 DKK
노르웨이 NOK
사우디아라비아 SAR
쿠웨이트 KWD
바레인 BHD
아랍에미리트 AED
요르단 JOD
이집트 EGP
태국 THB
싱가포르 SGD
말레이시아 MYR
인도네시아 IDR
카타르 QAR
카자흐스탄 KZT
브루나이 BND
인도 INR
파키스탄 PKR
방글라데시 BDT
필리핀 PHP
멕시코 MXN
브라질 BRL
베트남 VND
남아프리카 공화국 ZAR
러시아 RUB
헝가리 HUF
폴란드 PLN
'''
