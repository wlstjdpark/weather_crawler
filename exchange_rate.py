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
�̱� USD
�������� EUR
�Ϻ� JPY
�߱� CNY
ȫ�� HKD
�븸 TWD
���� GBP
���� OMR
ĳ���� CAD
������ CHF
������ SEK
ȣ�� AUD
�������� NZD
ü�� CZK
ĥ�� CLP
��Ű TRY
���� MNT
�̽��� ILS
����ũ DKK
�븣���� NOK
����ƶ��� SAR
�����Ʈ KWD
�ٷ��� BHD
�ƶ����̸�Ʈ AED
�丣�� JOD
����Ʈ EGP
�±� THB
�̰����� SGD
�����̽þ� MYR
�ε��׽þ� IDR
īŸ�� QAR
ī���彺ź KZT
��糪�� BND
�ε� INR
��Ű��ź PKR
��۶󵥽� BDT
�ʸ��� PHP
�߽��� MXN
����� BRL
��Ʈ�� VND
��������ī ��ȭ�� ZAR
���þ� RUB
�밡�� HUF
������ PLN
'''
