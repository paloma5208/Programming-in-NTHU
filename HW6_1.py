# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:34:12 2020

@author: Paloma
"""

"""
請利用正規運算式 , 驗證使用者輸入的帳號和密碼是否符合下列條件：

帳號
可使用英文字母、數字和半形句號（不一定都要出現）

密碼：
八個字元以上，且包含英文字母、數字和符號 （都必須出現
帳號不符合就印出“帳號格式錯誤”；密碼不符合就印出“密碼格式錯誤”；都符合就印出“通過測試”
"""

import re

#帳號pat
pattern1 = '^[\w\.]+$'

#密碼pat
pattern2 = '^(?=.*\d)(?=.*[a-zA-Z])(?=.*\W)\S{8,}'

def check_info(pattern1, pattern2):
    
    flag1 = False
    flag2 = False
    
    account = input('請輸入任意英文字母、數字、或半形句號: ')
    if re.match(pattern1, account):
        flag1 = True
    else:
        print('帳號格式錯誤')
        return
    
    password = input('請輸入八個字元以上，且包含英文字母、數字和符號的密碼: ')
    if re.match(pattern2, password):
        flag2 = True
    else:
        print('密碼格式錯誤')
        return
        
    if flag1 == True and flag2 == True:
        print('通過測試')
        return 
    
check_info(pattern1, pattern2)
