# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:29:01 2020

@author: Paloma
"""



import json

def get_reward(path):
    with open (path, 'r') as f:
        price = json.load(f)
    bull_reward = []
    bear_reward = []
    
    for i in range(0, len(price)):
        if price[i]['bullish_target_open_price'] == 'NaN' or\
           price[i]['bullish_target_close_price'] == 'NaN' or\
           price[i]['bearish_target_open_price'] == 'NaN' or\
           price[i]['bearish_target_close_price'] == 'NaN':
               continue
        
        bull_reward.append((price[i]['bullish_target_open_price'] - \
                            price[i]['bullish_target_close_price']) / \
                            price[i]['bullish_target_open_price'])
    
        bear_reward.append((price[i]['bullish_target_open_price'] - \
                            price[i]['bullish_target_close_price']) / \
                            price[i]['bullish_target_open_price'])
    
    return bull_reward, bear_reward
    
    

"""
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

path = 'backtest_targets_price.json'
bull_reward, bear_reward = get_reward(path)
all_reward = bull_reward + bear_reward 

plt.hist(all_reward, bins=40, range = [-1, 1], normed=0, facecolor="orange", edgecolor="black", alpha=0.7)
plt.title('Results')
plt.show()

plt.hist(bull_reward, bins=40, range = [-1, 1], normed=0, facecolor="orange", edgecolor="black", alpha=0.7)
plt.title('Bullish Results')
plt.show()

plt.hist(bear_reward, bins=40, range = [-1, 1], normed=0, facecolor="orange", edgecolor="black", alpha=0.7)
plt.title('Bearish Results')
plt.show()

