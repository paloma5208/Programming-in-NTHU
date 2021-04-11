# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:02:41 2020

@author: Paloma
"""

"""
期中專題
寫程式碼把需要的股價都抓下來
#一切順利，運行到一半會出現 ERROR: execution aborted
"""

import json
from HW3_1_teacher import * #getPriceData func. #如果是import HW3_1_teacher，就要用(HW3_1_teacher.)去call func.

#先把標的資訊全部都load進來，超多的喔！
backtest_targets_path = r"D:\Users\Paloma\Desktop\programming\week4_teacher_data\backtest_targets.json"
with open(backtest_targets_path, 'r') as f:
    target = json.load(f)

#有些公司已下市，暫時先不處理這些資料
t = ['3598', '4733', '3315', '6145', '2837']
new_data = []
for i in range(0, len(target)):
    if target[i]['bullish_target'] in t or target[i]['bearish_target'] in t:
        continue
     
    new_data.append(target[i])

with open('backtest_targets_remove_delist_target.json', 'w') as outfile:
    json.dump(new_data, outfile)

backtest_targets_remove_delist_target_path = r"D:\Users\Paloma\Desktop\programming\backtest_targets_remove_delist_target.json"

with open(backtest_targets_remove_delist_target_path, 'r') as f:
    target = json.load(f)
#target[1] >> {'year': '100','month': '1','bullish_target': '9933','bearish_target': '9902'}


target_list = []
for i in range(0, len(target)):    
    #len(target) >> 3464
    
    #以下兩行是把每個看漲、看跌標的抓下來
    #問題點：如何決定看漲和看跌標的？
    target_list.append(target[i]['bullish_target'])    
    #target[1] >> {'year': '100', 'month': '1', 'bullish_target': '9933', 'bearish_target': '9902'}
    #target[i]['bullish_target'] >> '9933'
    
    target_list.append(target[i]['bearish_target'])
    
target_set = list(set(target_list))
#target_set[1] >> '1418'
#len(target_set) >> 597

print("Hi")

for i in range(0, len(target_set)):
    
    #一直抓yahoo股價，IP位置會被封鎖，所以每抓30次就要休息個50秒
    if i % 30 == 1:
        time.sleep(10)
    
    print("go")
    getPriceData(target_set[i], '2000-01-03', '2020-03-20')

"""
一樣是期中專題的上課內容：找出指定區間的價格資訊
只抓2011年

2011年2月~2011年3月
"""

import pandas as pd
import datetime
from dateutil.relativedelta import * #做月份的加減

y = '100'
m = '1'

bullish_target = '1713'
bearish_target = '2022'

y = str(int(y) + 1911)
if len(m) < 2:
    
    #讓他變成date的格式
    m = '0' + m 

#一月開始投資，二月的11號可以買OR賣，三月的10號也買或賣，三月的11號也買或賣
#為了讓他可以加月份，所以用strptime
open_day = datetime.datetime.strptime(y + '-' + m + '-' + '11', '%Y-%m-%d') + relativedelta(month=+1)
close_day = datetime.datetime.strptime(y + '-' + m + '-' + '10', '%Y-%m-%d') + relativedelta(month=+2)

price_data = pd.read_csv(bullish_target + '.csv')

date_list = price_data['Date'].tolist()
start_date = datetime.datetime.strftime(open_day, '%Y-%m')
end_date = datetime.datetime.strftime(close_day, '%Y-%m')

check_start = 0    #有沒有找到開盤日
check_end = 0    #有沒有找到收盤日

for i in range(0, len(date_list)):
    if check_start == 0 and start_date == date_list[i]:    #如果還沒有找到開盤日，然後在list裡面發現開盤日，就把他的位置記下來，然後變成1，代表他已經找到ㄌ
        start_idx = i                                      #start_idx和end_idx是代表最後的日期要抓哪些區間
        check_start = 1
    elif check_end == 0 and end_date == date_list[i]:      #如果還沒找到收盤日，然後在list裡面發現開盤日，就把他的位置記下來，然後變成1，代表他已經找到ㄌ
        check_end = 1                                       
        end_idx = i + 1
        break
    
print(date_list[start_idx:end_idx])
"""
"""
#上一張
trade_range = price_data.iloc[start_idx:end_idx]
trade_date_list = trade_range['Date'].tolist()
for i in range(0, len(trade_date_list)):
    trade_date_list[i] = datetime.datetime.strptime(trade_date_list[i], '%Y-%m-%d')
    
open_delta = []
close_delta = []
for i in range(0, len(trade_date_list)):
    open_delta.append(abs(trade_date_list[i] - open_day))  #datetime這個class可能定義了'+'這個符號
    if trade_date_list[i] > close_day:
        continue
    else:
        close_delta.append(abs(trade_date_list[i] - close_day))
print(type(trade_date_list[i] - close_day))
#enumerate會回傳兩個東西，第一個是索引，第二個是值，分別是i、x
#i for i 前面的 i 是要被放到 open_indices裡面的東西
#簡單來說，從for開始之後就是i的條件
#for i, x in enumerate(open_delta):
#        if x == min(open_delta):
#            open_indices.append(i)
open_indices = [i for i, x in enumerate(open_delta) if x == min(open_delta)]  
close_indices = [i for i, x in enumerate(close_delta) if x == min(close_delta)]

open_idx = open_indices[-1]
close_idx = close_indices[-1]

trade_range = trade_range.reset_index()
open_price = trade_range['Adj Close'][open_idx]
close_price = trade_range['Adj Close'][close_idx]

"""
找出兩個標的的開盤收盤價
"""

backtest_targets_path = r"D:\Users\Paloma\Desktop\programming\week4_teacher_data\backtest_targets_remove_delist_target.json"
with open(backtest_targets_path, r) as f:
    target = json.load(f)
    


"""
計算最終平均損益
"""

import json
with open('backtest_results.json', 'r') as f:
    target = json.load(f)
    
bullish_return = []
bearish_return = []

for i in range(0, len(target)):
    if target[i]['bullish_target_open_price'] == 'NAN' or  \
       target[i]['bullish_target_close_price'] == 'NAN' or \
       target[i]['bearish_target_open_price'] == 'NAN' or  \
       target[i]['bearish_target_open_price'] == 'NAN':
       
       continue
    
    #做多>>先買後賣
    #做空放空>>先賣後買
    ##假設成本就是買進賣出當下的股價  
    
    #做多損益
    #(賣出價格 - 買進價格 )/ 買進價格
    #做空損益
    #(賣出價格 - 買進價格 )/ 賣出價格
    bullish_return.append((target[i]['bullish_target_close_price'] - \
                           target[i]['bullish_target_open_price']) / \
                            target[i]['bullish_target_open_price'])
    
    bearish_return.append((target[i]['bullish_target_open_price'] - \
                           target[i]['bullish_target_open_price']) / \
                            target[i]['bullish_target_open_price'])
    
avg_return = sum(bullish_return + bearish_return) / len(bullish_return + bearish_return)

                            





