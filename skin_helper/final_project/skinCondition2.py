# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:08:20 2020

@author: USER
"""

def Condition2(oil,water):
    if oil == "1" and water == "1":
        skinCondition = '1'
        return skinCondition
    
    elif oil == "1" and water == "2" :
        skinCondition = '2'
        return skinCondition
    
    elif oil == "2" and water == "1" :
        skinCondition = '3'
        return skinCondition
    
    elif oil == "2" and water == "2" :
        skinCondition = '4'
        return skinCondition
    
    elif oil == "3" and water == "1" :
        skinCondition = '5'      
        return skinCondition
    
    elif oil == "3" and water == "2" :
        skinCondition = '6'
        return skinCondition