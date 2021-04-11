# -*- coding: utf-8 -*-
"""
Created on Sat May 5 10:20:54 2020

@author: user
"""
import os
import re
import pickle
import json
from history_record_class import *
import datetime

def checkPassword(password):

    output = "true"
    #檢查密碼長度是否大於等於8
    pattern2 = r"\S{8,}"
    if not re.fullmatch(pattern2, password):
        output = "false"
        print(1)

    #檢查密碼是否出現英文字母、數字     
    pattern3 = r"[0-9]"
    pattern4 = r"[a-zA-Z]"

    check1 = re.findall(pattern3, password)
    check2 = re.findall(pattern4, password)
    #若有一項沒出現該項的check長度為0
    if len(check1) == 0 or len(check2) == 0:
        output = "false"
        print(2)

    character_list = list(set(password))
    candidate = []
    for i in range(0,len(character_list)):#判斷是否有三個重複字元相連
        candidate.append(character_list[i]*3)

    for i in range(0,len(candidate)):
        if candidate[i] in password:
            output = "false"
            print(3)

    return output

def newAccount():
    name = input("請輸入姓名:")
    mail = input("請輸入電子郵件:")
    filename = mail + '.pkl'
    
    if filename not in os.listdir('./info'):
        password = input('請輸入密碼:')
        while True:
            output = checkPassword(password)
            if output == "false":
                password = input("密碼不符合規定，請重新輸入:")
                continue
            else:
                break
        data = Customer(name, mail, password, info = [])
        saveAccount(filename,data)
    else:
        print('已有可用帳戶')

def newAccount2(name, mail, password):

    filename = mail + '.pkl'

    data = Customer(name, mail, password)
    saveAccount(filename,data)


def saveAccount(filename,data):
    with open('./info/login_info/' + filename , 'wb') as f:
        pickle.dump(data,f)


def openAccount(filename):
    with open('./info/login_info/' + filename +'.pkl', 'rb') as f:
        data = pickle.load(f)
    return data

def saveInfo(name, condition, cause):
    filename = name + '.json'
    nowtime = datetime.datetime.now()
    y = nowtime.year
    m = nowtime.month
    d = nowtime.day
    today = str(y) + '-' + str(m) + '-' + str(d)
    if filename in os.listdir('./info/record/'):
        with open('./info/record/' + filename , 'r') as f:
            tmp = json.load(f)        
        data = '日期:'+ today+','+'膚況:'+ condition+','+'原因:'+cause
        tmp.append(data)
        with open('./info/record/' + filename , 'w') as f:
            json.dump(tmp,f)
    else:
        tmp = []
        data = '日期:'+ today+','+'膚況:'+ condition+','+'原因:'+cause
        tmp.append(data)
        with open('./info/record/' + filename , 'w') as f:
            json.dump(tmp,f)
        
def openInfo(name):
    filename = name + '.json'
    with open('./info/record/' + filename , 'r') as f:
        data = json.load(f)
    return data