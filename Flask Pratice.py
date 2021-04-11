# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:48:53 2020

@author: Paloma
"""

"""
可用flask呈現我們的期末

"""
from flask import Flask, request
from flask import render_template

# __name__: #幫app(網頁應用程式)命名
app = Flask(__name__) 

#POST是瀏覽器跟伺服器端某種溝通的方法
#GET 可以解決method not allow的問題
@app.route('/login', methods = ['GET', 'POST']) 
def login():
    
    #利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
        return 'Hello ' + request.values['username']

    return  "<form method='post' action='/login'>" \
            "<input type='text' name='username' />" \
            "</br>" \
            "<button type='submit'>Submit</button>" \
            "</form>"
            
if __name__ == '__main__': 
    app.run()
    
"""
"""
from flask import Flask, request
from flask import render_template

# __name__: #幫app(網頁應用程式)命名
app = Flask(__name__) 

#POST是瀏覽器跟伺服器端某種溝通的方法
#GET 可以解決method not allow的問題
@app.route('/login', methods = ['GET', 'POST']) 
def login():
    
    #利用request取得使用者端傳來的方法為何
    if request.method == 'POST':
        return 'Hello ' + request.values['username']

    #非post的時候回傳空白模板
    #把字串存成html檔
    return render_template('login.html')
            
if __name__ == '__main__': 
    app.run() 

"""
重新導向
"""

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/loginurl', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('hello', username = request.form.get('username')))
    
    return render_template('login.html')

@app.route('/hello/<username>')
def hello(username):
    return render_template('variable1.html', name = username)
    
if __name__ == '__main__': 
    app.run() 

            
#這是我自己電腦裡面的路徑 (在local) 
#裝飾器: 當路徑後面是5000(沒有東西)或是一條反斜線，就會自動執行這個函式 
@app.route('/') 

#只要執行程式，就會自動把這個html檔抓進去網頁並呈現 
#一定要有一個叫做templates的資料夾QAQ 
#從網址裡面抓name的值
def index():
    
    input_name = request.args.get('name')
    input_id = request.args.get('id')
    
    #多個變數時用字典整理較簡潔
    user_info = {
        'name': input_name,
        'id':input_id
    }
    
    return render_template('variable2.html', **user_info) #兩個星星代表不指定變數長度

@app.route('/hello/') #有了變數之後網頁可以個人化顯示 #網址也要跟著改喔
def hello_name():
    name = request.args.get('name') #從網址中取出我要的變數名稱
    surname = request.args.get('surname')
    return '<h1> Hello, {} {}</h1>'.format(name, surname)

@app.route('/QF')#設新的路徑 #分網頁的頁面類似網站首頁XD #類似網頁子頁面 
def hello1():
    return 'Hello，QF!'


if __name__ == '__main__': #如果是直接執行這個script，就代表這個script是主程式 #意思:如果我現在執行的script是主程式
    app.run() #執行這個模組

