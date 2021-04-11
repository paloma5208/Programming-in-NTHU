# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:42:37 2020

@author: Paloma
"""

import requests
import re
from bs4 import BeautifulSoup

#抓品名
def get_name(soup_info, name_list):

    #用re套件去除多餘字元
    for i in range(0, len(soup_info)):
        name = soup_info[i].h3.text
        name = re.sub('[\xa0\n\t]', '', name)
        name_list.append(name)

#抓商品價格
def get_price(soup_info, price_list):

    for i in range(0, len(soup_info)):
        
        price = soup_info[i].div.text
        price_list.append(price)

#抓品項總頁數
#頁數紀錄在maxpagenoid屬性中
#.get('屬性名稱')可獲取屬性值
def get_page_num(soup):
    
    #soup.find_all('div', 'PLP-Filter3')是list, 所以用for迴圈抓裡面資料
    for data in soup.find_all('div', 'PLP-Filter3'):
        page_num = data.get('data-maxpagenoid')
    
    return page_num