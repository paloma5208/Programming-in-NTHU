# -*- coding: utf-8 -*-
"""
Created on Sat May 23 00:01:08 2020

@author: Paloma
"""

import HW_1_1 #執行程式時會先執行HW1_1的script
import pickle

from flask import Flask, request, render_template, redirect, url_for, flash
import os 

os.chdir(r"D:\Users\Paloma\Desktop\programming")
app = Flask(__name__)


@app.route('/login', methods = ['GET', 'POST']) #在網址後面輸入/login
def login():

    if request.method == 'POST':
        username = request.values['username']
        with open(username + '.pkl','rb') as f:
            username = pickle.load(f)
        return '餘額:' + str(username.getBalance())

    return render_template('checkCreditCard.html')

if __name__ == '__main__':
    app.run()

