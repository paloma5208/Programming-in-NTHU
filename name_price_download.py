# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 01:08:24 2020

@author: Paloma
"""

#引入撰寫爬蟲所需套件

import requests
import re
from bs4 import BeautifulSoup
import os
from name_price_download_func import *

os.chdir("D:\\Users\\Paloma\\Desktop\\finalproject")

"""
爬toner品項+價格的主程式
"""

headers = {
        'User-Agent': 'Googlebot'
}

#設空list當作函式參數
toner_name_list = []
toner_price_list = []

#為了獲取總頁數，要先抓網頁
url = 'https://www.watsons.com.tw/search2?text=%E5%8C%96%E5%A6%9D%E6%B0%B4'
res = requests.get(url, headers = headers, allow_redirects = False)
soup = BeautifulSoup(res.text, 'lxml')
toner_page_num = int(get_page_num(soup))


for i in range(0, toner_page_num):
    url_page = 'https://www.watsons.com.tw/search2?text=%E5%8C%96%E5%A6%9D%E6%B0%B4&page=' + str(i) + '&resultsForPage=32&min=&max=&level=1&cid=&parentCid=&filter=&sort='
    res = requests.get(url_page, headers = headers, allow_redirects = False)
    soup = BeautifulSoup(res.text, 'lxml')
    toner = soup.find_all('div', 'productNameInfo')
    get_name(toner, toner_name_list)
    get_price(toner, toner_price_list)

#用長度檢查品項&價格是否匹配
len(toner_price_list) == len(toner_name_list)

"""
爬essence品項+價格的主程式
"""

headers = {
        'User-Agent': 'Googlebot'
}

#設空list當作函式參數
essence_name_list = []
essence_price_list = []

#為了獲取總頁數，要先抓網頁
url = 'https://www.watsons.com.tw/search2?text=%E7%B2%BE%E8%8F%AF%E6%B6%B2'
res = requests.get(url, headers = headers, allow_redirects = False)
soup = BeautifulSoup(res.text, 'lxml')
essence_page_num = int(get_page_num(soup))


for i in range(0, essence_page_num):
    url_page = 'https://www.watsons.com.tw/search2?text=%E7%B2%BE%E8%8F%AF%E6%B6%B2&page=' + str(i) + '&resultsForPage=32&min=&max=&level=1&cid=&parentCid=&filter=&sort='
    res = requests.get(url_page, headers = headers, allow_redirects = False)
    soup = BeautifulSoup(res.text, 'lxml')
    essence = soup.find_all('div', 'productNameInfo')
    get_name(essence, essence_name_list)
    get_price(essence, essence_price_list)

#用長度檢查品項&價格是否匹配
len(essence_price_list) == len(essence_name_list)

"""
爬gel品項+價格的主程式
"""

headers = {
        'User-Agent': 'Googlebot'
}

#設空list當作函式參數
gel_name_list = []
gel_price_list = []

#為了獲取總頁數，要先抓網頁
url = 'https://www.watsons.com.tw/search2?text=%E5%87%9D%E8%86%A0'
res = requests.get(url, headers = headers, allow_redirects = False)
soup = BeautifulSoup(res.text, 'lxml')
gel_page_num = int(get_page_num(soup))


for i in range(0, gel_page_num):
    url_page = 'https://www.watsons.com.tw/search2?text=%E5%87%9D%E8%86%A0&page=' + str(i) + '&resultsForPage=32&min=&max=&level=1&cid=&parentCid=&filter=&sort='
    res = requests.get(url_page, headers = headers, allow_redirects = False)
    soup = BeautifulSoup(res.text, 'lxml')
    gel = soup.find_all('div', 'productNameInfo')
    get_name(gel, gel_name_list)
    get_price(gel, gel_price_list)

#用長度檢查品項&價格是否匹配
len(gel_price_list) == len(gel_name_list)

"""
爬lotion品項+價格的主程式
"""
headers = {
        'User-Agent': 'Googlebot'
}

#設空list當作函式參數
lotion_name_list = []
lotion_price_list = []

#為了獲取總頁數，要先抓網頁
url = 'https://www.watsons.com.tw/search2?text=%E4%B9%B3%E6%B6%B2'
res = requests.get(url, headers = headers, allow_redirects = False)
soup = BeautifulSoup(res.text, 'lxml')
lotion_page_num = int(get_page_num(soup))


for i in range(0, lotion_page_num):
    url_page = 'https://www.watsons.com.tw/search2?text=%E4%B9%B3%E6%B6%B2&page=' + str(i) + '&resultsForPage=32&min=&max=&level=1&cid=&parentCid=&filter=&sort='
    res = requests.get(url_page, headers = headers, allow_redirects = False)
    soup = BeautifulSoup(res.text, 'lxml')
    lotion = soup.find_all('div', 'productNameInfo')
    get_name(lotion, lotion_name_list)
    get_price(lotion, lotion_price_list)

#用長度檢查品項&價格是否匹配
len(lotion_price_list) == len(lotion_name_list)

"""
爬cream品項+價格的主程式
"""
headers = {
        'User-Agent': 'Googlebot'
}

#設空list當作函式參數
cream_name_list = []
cream_price_list = []

#獲取總頁數
url = 'https://www.watsons.com.tw/search2?text=%E4%B9%B3%E9%9C%9C'
res = requests.get(url, headers = headers, allow_redirects = False)
soup = BeautifulSoup(res.text, 'lxml')
cream_page_num = int(get_page_num(soup))


for i in range(0, cream_page_num):
    url_page = 'https://www.watsons.com.tw/search2?text=%E4%B9%B3%E9%9C%9C&page=' + str(i) + '&resultsForPage=32&min=&max=&level=1&cid=&parentCid=&filter=&sort='
    res = requests.get(url_page, headers = headers, allow_redirects = False)
    soup = BeautifulSoup(res.text, 'lxml')
    cream = soup.find_all('div', 'productNameInfo')
    get_name(cream, cream_name_list)
    get_price(cream, cream_price_list)

#用長度檢查品項&價格是否匹配
len(cream_price_list) == len(cream_name_list)

"""
把品名、價格存成字典
"""

toner_dict = {}
essence_dict = {}
gel_dict = {}
lotion_dict = {}
cream_dict = {}

#品名是索引，價格是value
counter = -1
for i in toner_name_list:
    counter += 1
    toner_dict[i] = toner_price_list[counter] 
    with open('toner_dict', 'w') as f:
        json.dump(toner_dict, f)

counter = -1
for i in essence_name_list:
    counter += 1
    essence_dict[i] = essence_price_list[counter]
    with open('essence_dict', 'w') as f:
        json.dump(essence_dict, f)

counter = -1
for i in gel_name_list:
    counter += 1
    gel_dict[i] = gel_price_list[counter]
    with open('gel_dict', 'w') as f:
        json.dump(gel_dict, f)

counter = -1
for i in lotion_name_list:
    counter += 1
    lotion_dict[i] = lotion_price_list[counter]
    with open('lotion_dict', 'w') as f:
        json.dump(lotion_dict, f)

counter = -1
for i in cream_name_list:
    counter += 1
    cream_dict[i] = cream_price_list[counter]
    with open('cream_dict', 'w') as f:
        json.dump(cream_dict, f)

"""
只爬適合使用者的品項
"""