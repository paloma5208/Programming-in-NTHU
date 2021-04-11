# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:11:02 2020

@author: Paloma
"""

from plotly.offline import plot, iplot, init_notebook_mode
import plotly.graph_objs as go
import pandas_datareader as web
from datetime import datetime
import pandas as pd

def get_k(target):
    price = pd.read_csv(target + '.csv')

    trace = go.Candlestick(x = price['Date'],
                           open = price['Open'],
                           high = price['High'],
                           low = price['Low'],
                           close = price['Close'])
    data = [trace]

    return data

data = get_k('2330')
plot(data)
