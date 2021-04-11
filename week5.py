# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:30:42 2020

@author: Paloma
"""
"""
例外處理
"""
#平常寫程式遇到錯誤會停在錯誤的地方，但例外處理可以幫我們
#1.略過他
#2.用不一樣的方式處理錯誤

#如果符合TRY的話，就不會跳出錯誤訊息

def fetcher(obj, index):
    return obj[index]

#ez1
x = 'apple'
print(fetcher(x, 4))

"""
"""

#ez2

def fetcher(obj, index):
    return obj[index]

print(fetcher(x, 5))

"""
"""

def fetcher(obj, index):
    return obj[index]

try:
    print(fetcher(x,5))
    
except IndexError:
    print('Get exception')
   
"""
"""
    
def fetcher(obj, index):
    return obj[index]
    
try:
    print(fetcher(x, 5))
except IndexError:
    print('Get exception')
    
print('Continuing')

"""
"""
x = [1, 2, 3]
y = 'apple'

try:
    x[0] + y[0] #typeerror
    
except TypeError:
    print('E1')
    
except IndexError as e:
    print(e)
    
except(NameError, KeyError):
    print('E3')
    
except:
    print('E4')
    
else:
    print('No Exception')

"""
"""

try:
    print(x[10]) #indexerror
    
except TypeError:
    print('E1')
    
except IndexError as e:
    print(e)
    
except(NameError, KeyError):
    print('E3')
    
except:
    print('E4')
    
else:
    print('No Exception')
    
"""
"""
    
try:
    a(x, y) #nameerror
    
except TypeError:
    print('E1')
    
except IndexError as e:
    print(e)
    
except(NameError, KeyError):
    print('E3')
    
except:
    print('E4')
    
else:
    print('No Exception')
    
"""
"""
    
try:
    b = 4/0 #zerodivisionerror
    
except TypeError:
    print('E1')
    
except IndexError as e:
    print(e)
    
except(NameError, KeyError):
    print('E3')
    
except: #有錯誤，但錯誤不在上述範圍內
    print('E4')
    
else:
    print('No Exception')
    
"""
"""
    
try:
    c = 1 + 1 #no exception
    
except TypeError:
    print('E1')
    
except IndexError as e:
    print(e)
    
except(NameError, KeyError):
    print('E3')
    
except:
    print('E4')
    
else:
    print('No Exception')
    
"""
"""
#不管有錯或沒錯，都會執行finally
try:
    b = 4/0 #zerodivisionerror
    
except TypeError:
    print('E1')
    
except IndexError as e:
    print(e)
    
except(NameError, KeyError):
    print('E3')
    
except: #有錯誤，但錯誤不在上述範圍內
    print('E4')
    
else:
    print('No Exception')
    
finally:
    print('finally')
    
"""
"""

def raiseError1():
    raise IndexError #告訴你引發了哪些錯誤
    
raiseError1()

def raiseError2():
    raise IndexError('Error2') #Error2是提示
    
raiseError2

"""
"""

a = input('輸入一個整數: ')
if not a.isdigit():
    raise ValueError('a 必須是整數')
    
"""
assert
"""
#assert負責做變數確認
#ex1
"""
"""
assert a

"""
"""
a = 1
assert a < 0, 'a must be negative' #前面是條件，後面是解釋

"""
"""
#每個error都是一個class
#定義一個新的例外狀況叫做mybad
# __str__ call他時就會回傳string

class MyBad(Exception):
    def __str__(self): #這是固定用法喔
        return 'Sorry! my mistake!'
    
a = 1
b = 2
if a != b:
    raise MyBad
    
"""
try/except其他用法
"""

while True:
    for i in range(0, 10):
        if i > 3:
            break   #這邊的break只會離開for迴圈，所以這段程式永遠離不開while迴圈
        print(i)
        
        
"""
"""
while True:
    for i in range(0, 10):
        if i > 3:
            break
        print(i)
    else: #是跟for對應喔！（算是比較特別的用法）
        continue
    
    break
"""
""" 
class Exitloop(Exception):
    pass　#pass指部執行任何事情 #對了ctrl+c可以停止迴圈

try:
    while True:
        for i in range(0, 10):
            if i > 3:
                raise Exitloop #提出錯誤，讓整個程式停止
            print(i)
except Exitloop:
    print('Stop')

"""
記錄錯誤資訊但不影響程式碼執行
"""

import traceback #有錯誤時可以把錯誤存在某個檔案裏面，

def inverse(x):
    return 1/x

try:
    inverse(0)
except: #將錯誤記在你打開的這個文件
    traceback.print_exc(file = open('9_traceback.exc,', 'w'))
    