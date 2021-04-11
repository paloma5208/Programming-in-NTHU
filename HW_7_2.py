# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:58:57 2020

@author: Paloma
"""
import os #改工作資料夾
import pandas as pd #處理csv
from sklearn.utils import shuffle #搖資料
from sklearn import svm #機器學習
from sklearn.metrics import accuracy_score #算預測準確度

os.chdir(r'D:\Users\Paloma\Desktop\programming\0519_info')
data = pd.read_csv('HW7_2.csv')

#把Y, N用數字表示
ecfg = pd.get_dummies(data.ecfg)
flbmk = pd.get_dummies(data.flbmk)
flg_3dsmk = pd.get_dummies(data.flg_3dsmk)
insfg = pd.get_dummies(data.insfg)
ovrlt = pd.get_dummies(data.ovrlt)

#data = data.drop(['flbmk'], axis = 1) #flbmk欄位資訊沒有變化，對預測不造成影響，故可移除
dummy_ecfg = ecfg['Y'].tolist()
dummy_flg_3dsmk = flg_3dsmk['Y'].tolist()
dummy_insfg = insfg['Y'].tolist()
dummy_ovrlt = ovrlt['Y'].tolist()
dummy_flbmk = flbmk['Y'].tolist()

#把原始資料的Y, N用數字替換
data['ecfg'] = dummy_ecfg
data['flg_3dsmk'] = dummy_flg_3dsmk
data['insfg'] = dummy_insfg
data['ovrlt'] = dummy_ovrlt
data['flbmk'] = dummy_flbmk

value_1 = data[0:1100] #全為1，共1100筆
value_0 = data[1100:] #全為0，共1100筆

train_value_1 = value_1[0:1000] #全為1，共1000筆
train_value_0 = value_0[0:1000] #全為0，共1000筆

test_value_1 = value_1[1000:] #全為1，共100筆
test_value_0 = value_0[1000:] #全為1，共100筆

#合併後，使得fraud_ind欄位的兩相異值，在train和test中比例皆為1:1
#打亂資料
train_data = pd.concat([train_value_1, train_value_0], ignore_index=True)
new_train_data = shuffle(train_data)
new_train_data.index = range(0, len(new_train_data))

test_data = pd.concat([test_value_1, test_value_0], ignore_index=True)
new_test_data = shuffle(test_data)
new_test_data.index = range(0, len(new_test_data))

#將資料分成訓練和測試
train_x = new_train_data.drop(['fraud_ind'], axis = 1)
test_x = new_test_data.drop(['fraud_ind'], axis = 1)
train_y = new_train_data['fraud_ind']
test_y = new_test_data['fraud_ind']

clf = svm.SVC()
clf.fit(train_x, train_y)

prediction = clf.predict(test_x)
accuracy = accuracy_score(test_y, prediction)

#svm準確度: 0.5
print(accuracy)

"""
"""
from sklearn import tree

train_x = new_train_data.drop(['fraud_ind'], axis = 1).values.tolist()
test_x = new_test_data.drop(['fraud_ind'], axis = 1).values.tolist()
train_y = new_train_data['fraud_ind']
test_y = new_test_data['fraud_ind']

clf = tree.DecisionTreeClassifier()
clf.fit(train_x, train_y)

prediction = clf.predict(test_x)
print(prediction)
accuracy = accuracy_score(test_y, prediction)

#decision tree準確度: 0.94
print(accuracy)
