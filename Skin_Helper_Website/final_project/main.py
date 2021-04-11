# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 12:21:29 2020

@author: Paloma
"""

from flask import *
from history_record_class import *
from history_record_functions import *
from skinCondition1 import*
from skinCondition2 import*
from 語錄系統 import*

from myapplication import app
app.run(debug=True)

app = Flask(__name__)

@app.route('/start', methods = ['GET', 'POST'])
def start():
    return render_template('start_main_page.html')

@app.route('/create_account', methods = ['GET', 'POST'])
def create_account():

    if request.method == 'POST':
        user_name = request.values['user_name']
        user_account = request.values['user_email']
        user_pwd = request.values['user_pwd']

        if checkPassword(user_pwd) == 'false':
            return render_template('create_account.html')
        else:
            newAccount2(user_name, user_account, user_pwd)
            return render_template('create_transform.html')

    return render_template('create_account.html')

@app.route('/create_transform', methods = ['GET', 'POST'])
def create_transform():
    return render_template('create_transform.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():

    if request.method == 'POST':

        user_account = request.values['user_email']
        user_pwd = request.values['user_pwd']

        try:
            user = openAccount(user_account)
        except:
            return render_template('login.html')

        flag = 0
        if user_account == user.mail:
            flag += 1
        if user_pwd == user.password:
            flag += 1
        if flag == 2:
            global account
            account = user_account
            return render_template('home.html')
        else:
            return render_template('login.html')
    
    return render_template('login.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html') #傳回網頁

@app.route('/record', methods=['GET', 'POST'])
def record():
    if request.method == 'POST':
        name = account
        condition = str(request.form['condition'])
        cause = str(request.form['cause'])
        saveInfo(name, condition, cause)
        name = account
        data = openInfo(name)
        string = ''
        for i in range(0,len(data)):
            string = string + data[i] + '\n'        
        info = {"info":string}
        return render_template('skin_condition.html', **info)
    return render_template('skin_record.html') #傳回網頁

@app.route('/skincondition', methods=['GET', 'POST'])
def skincondition():
    name = account
    data = openInfo(name)
    string = ''
    for i in range(0,len(data)):
        string = string + data[i] + '\n'        
    info = {"info":string}
    return render_template('skin_condition.html', **info) 

@app.route('/known', methods=['GET', 'POST'])
def known():
    if request.method == 'POST':
        num = str(request.form["number"])
        result1 = Condition1(num)
        word = wordchoose()
        word_list = { "word":word }
        if result1 == "1":
            return render_template('transform_控油化妝水.html', **word_list)
        if result1 == "2":
            return render_template('transform_凝膠.html', **word_list)
        if result1 == "3":
            return render_template('transform_乳液.html', **word_list)
        if result1 == "4":
            return render_template('transform_補水型化妝水.html', **word_list)
        if result1 == "5":
            return render_template('transform_精華液.html', **word_list)
        if result1 == "6":
            return render_template('transform_乳霜.html', **word_list)
        
    return render_template('known.html') #傳回網頁


@app.route('/unknown', methods=['GET', 'POST'])
def unknown():
    if request.method == 'POST':
        num1 = str(request.form['number1'])
        num2 = str(request.form['number2'])
        result2 = Condition2(num1,num2)
        word = wordchoose()
        word_list = { "word":word }
        if result2 == "1":
            return render_template('transform_控油化妝水.html', **word_list) #傳回網頁
        if result2 == "2":
            return render_template('transform_凝膠.html', **word_list)
        if result2 == "3":
            return render_template('transform_乳液.html', **word_list)
        if result2 == "4":
            return render_template('transform_補水型化妝水.html', **word_list)
        if result2 == "5":
            return render_template('transform_精華液.html', **word_list)
        if result2 == "6":
            return render_template('transform_乳霜.html', **word_list)
        
    return render_template('unknown.html') #傳回網頁

@app.route('/transform_1', methods=['GET', 'POST'])
def transform_1():
    word = wordchoose()
    word_list = { "word":word }
    return render_template('transform_控油化妝水.html', **word_list) #傳回網頁

@app.route('/transform_2', methods=['GET', 'POST'])
def transform_2():
    word = wordchoose()
    word_list = { "word":word }
    return render_template('transform_凝膠.html', **word_list) #傳回網頁

@app.route('/transform_3', methods=['GET', 'POST'])
def transform_3():
    word = wordchoose()
    word_list = { "word":word }
    return render_template('transform_乳液.html', **word_list) #傳回網頁

@app.route('/transform_4', methods=['GET', 'POST'])
def transform_4():
    word = wordchoose()
    word_list = { "word":word }
    return render_template('transform_補水型化妝水.html', **word_list) #傳回網頁

@app.route('/transform_5', methods=['GET', 'POST'])
def transform_5():
    word = wordchoose()
    word_list = { "word":word }
    return render_template('transform_精華.html', **word_list) #傳回網頁

@app.route('/transform_6', methods=['GET', 'POST'])
def transform_6():
    word = wordchoose()
    word_list = { "word":word }
    return render_template('transform_乳霜.html', **word_list) #傳回網頁

if __name__ == '__main__':
    app.run()(debug=True)


