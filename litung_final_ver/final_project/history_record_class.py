# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 16:04:27 2020

@author: user
"""
class Customer:
    def __init__ (self, name, mail, password):
        self.name = name
        self.mail = mail
        self.password = password
        
    def show_password(self):
        return self.password



