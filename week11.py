# -*- coding: utf-8 -*-
"""
Created on Sat May 30 21:52:13 2020

@author: Paloma
"""

import os #改工作資料夾
import pandas as pd
from sklearn.utils import shuffle
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

os.chdir(r'D:\Users\Paloma\Desktop\programming\0526info')


movies = pd.read_csv('movies.csv')

genres = []
for i in range(0, len(movies)):
    genres.append(movies['genres'][i].split('|'))

from sklearn.preprocessing import MultiLabelBinarizer #多標籤標記
tmp_genres = pd.Series(genres) #說明文件會標示套件要求何種格式

mlb = MultiLabelBinarizer() #建分類器

oneHotGenres = pd.DataFrame(mlb.fit_transform(tmp_genres), columns=mlb.classes_)

movie_feature = oneHotGenres.values.tolist() #將每部電影對應類型用0、1標記



rating = pd.read_csv('ratings.csv')
user_list = list(set(rating['userId'].tolist()))

group = rating.groupby('userId') #若userId相同，則放在同一組

cart = [] #將不同user看的電影各自用list存起來
rate = [] #將不同user對電影的評分各自用list存起來
for i in range(0, len(user_list)):
    tmp = group.get_group(user_list[i])
    cart.append(tmp['movieId'].tolist())
    rate.append(tmp['rating'].tolist())

user_feature = []

for i in range(0, len(cart)): #i: user看哪些電影
    tmp = [[]for n in range(20)]

    for j in range(0, len(cart[i])): #j: user看的特定電影
        movie_idx = list(movies['movieId']).index(cart[i][j]) #電影的index
        m_feature = movie_feature[movie_idx] #電影的類型
        indices = [m for m, x in enumerate(m_feature) if x == 1] #m存index，x存值，若x為1，則把m記下來

        for k in indices: #將特定電影評分記在tmp
            tmp[k].append(rate[i][j])

    avg_rate = []
    for j in range(0, len(tmp)):
        if len(tmp[j]) > 0:
            avg_rate.append(sum(tmp[j])/len(tmp[j])) #user對某類電影的總評分/某類電影的數量
        else:
            avg_rate.append(0)

    user_feature.append(avg_rate) #每個user對各個電影類型的平均評分

#給定電影題材，判斷該使用者對這部電影的評分
#做法: input[電影題材]+[使用者特徵]output分數
movie_idList = movies['movieId'].tolist()

model_input = []
model_output = []
for i in range(0, len(rating)):
    user_id = rating['userId'][i] - 1
    u_feature = user_feature[user_id] #特定user對電影類型的平均評分

    movie_id = movie_idList.index(rating['movieId'][i]) #特定電影的index
    m_feature = movie_feature[movie_id] #特定電影的類型

    tmp = u_feature + m_feature

    model_input.append(tmp) #user對不同類型的平均給分+電影類型
    model_output.append(rating['rating'][i]) #user實際上對電影的給分

X, Y = shuffle(model_input, model_output)

train_x = X[0:100]
train_y = Y[0:100]

test_x = X[100:1000]
test_y = Y[100:1000]

clf = SVR(kernel='rbf', C=1e3, gamma=0.1)
clf.fit(train_x, train_y)

prediction = clf.predict(test_x)

score = mean_squared_error(test_y, prediction)