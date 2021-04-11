# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:50:59 2020

@author: Paloma
"""

#Decorator
#可以傳func1.當參數，傳在func2.裡面，最後func2.回傳的是func1.
def print_func_name(func):
    def wrap():
        print("Now use function '{}'".format(func.__name__))
        func()
    return wrap #這邊回傳的是一個func

def dog_bark():
    print('Bark!!!')
    
def cat_miaow():
    print('Miaow~~~')
    
print_func_name(dog_bark)() 
#平常要執行一個func的時候後面都會有一個空括弧(指最後的括弧)，這行的意思就意思是wrap()
#注意喔我們傳的是func不是func的結果，最終回傳的也不是func的結果而是另外一個func


print_func_name(cat_miaow)()

"""
"""
#現在我們要做的就是簡化上面的東西
# @就是decarator，它可以幫助我們把下面的傳進去指定的函數
# 

def print_func_name(func):
    def wrap():
        print("Now use function '{}'".format(func.__name__))
        func()
    return wrap

@print_func_name
def dog_bark():
    print('Bark !!!')
    
@print_func_name
def cat_miaow():
    print('Miaow ~~~')
    
"""
"""
#先傳後執行(stack)
#先執行warp_1，再來是warp_2，再來是dog_bark
#dog_bark()是主程式，但執行的結果卻是最後才印出狗叫聲
#執行狗叫聲func之後傳到print_time裡面，現在print_time的func()就變成了狗叫聲
#縣再回傳的是warp_2這個func
#在來會往下一個@去傳，也就是print_func_name，現在這裡面的func()是warp_2
#現在回傳的是warp_1
#總而言之最後的結果是第一個被call的最後印出來，堆在上面的先被解決，最後才去處理狗叫聲的部分

import time

def print_func_name(func):
    def warp_1():
        print("Now use function '{}'".format(func.__name__))
        func()
    return warp_1

def print_time(func):
    def warp_2():
        print("Now the Unix time is {}". format(int(time.time())))
        func()
    return warp_2

@print_func_name
@print_time
def dog_bark():
    print('Bark !!!')
    
dog_bark()

"""
"""

#第一層定義接收一個變數，第二層才定義接收一個func
#上面的做法是從第二階開始
#但如果你想多加一個變數，就要在外面多用一階

def print_func_name(time):
    def decorator(func): #這邊的func是狗叫聲
        def warp():
            print("Now use function '{}'".format(func.__name__))
            print("Now Unix time is {}".format(int(time)))
            func()
        return warp
    return decorator
#最外層先接收了變數的部分，再來說要去執行dec這個func(指return decorator)，再來接收了狗叫聲這個func，再來執行warp


@print_func_name(time=(time.time())) #這個函數同時接收了一個變數(指time)和一個func
def dog_bark():
    print('Bark !!')
            
dog_bark() #這是主程式 #最後執行的結果是warp這個func傳過來

"""
"""
#Decorator & class

class Dog:
    def __init__(self, func):
        self.talent = func
        
    def bark(self):
        print('Bark !!')
        
@Dog #把run這個func傳進去dog這個class
def dog_can_run():
    print('Run')
    
@Dog
def dog_can_jump():
    print('Jump')

#dog1和dog2意思其實就是跟dog0一樣
dog_0 = Dog(dog_can_run)

dog_1 = dog_can_run
dog_1.talent()

dog_2 = dog_can_jump
dog_2.talent()

"""
"""
#@static method
#static method不需要也不能傳入變數self
#當我們不希望動到class的data attribute並且確定不用動到、是固定時，就可以用static method
#沒打完
class Shiba:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        
    @staticmethod
    def run(length):
        print('run' + '.' * length)
        
"""
"""
#class method
#傳class本身的資訊
class Shiba:
    
    length = 10 #這是class attribute
    
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        
    @classmethod
    def run(cls): #為了告訴這個func說這個func會用到原本的class attribute
        print('run' + '.' * cls.length) #會打class attribute拿來用
        
Shiba.run()

black_shiba = Shiba(90, 40)
black_shiba.run()

"""
"""
#當我們在func前面加兩條底線，代表這個func是私有的，也就是只有在class裡面可以使用她，再煮程式裡面不能直接call這個func
#為了不讓她跟外部的func混在一起

#在python裡面data attribute不是私有的，代表user可以隨意更改裡頭的資訊，例如我們覺得狗的名字不應該被亂改
#所以我們要去定義一個新的變數，當我們想取得狗狗的名字，

#@property定義底下的要回傳的東西是self._name
#為了讓名字是私有的

#當我們想要更改name時不能直接改了
#(black_shiba._name = 'rr'是直接改)
#現在希望user可以按照我們的方式去更改私有的名字

#我們當然可以直接改(Ex.'rr')
#但我們在寫程式時真的不希望user隨意去更動
#所以用property去設定一個變數(getter)
#如果要重新設定名字時就要用這個(setter)

#property很像是設定了一個data attribute(self.name)
#property 取得名字
#setter 獲得名字
#希望使用者按照我們的流程式設定名字，所以才會有這種機制
#為了設計成讓property的name很像data attribute，所以底下在呼叫時後面不用加括弧
#平常在執行class 裏頭的func時後面都會加一個括弧
#但property、setter的func後面不用再加括弧
#然後設定名字直接用等號即可

#透過定義getter(取得)跟setter(設定)，讓這些事情有一個間接的過程

"""
"""
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    @property #讓大家知道不能直接取得password，但能取得password的hash
    def password(self):
        raise AttributeError('password is not readable attribute')
        
    @password.setter
    def setPassword(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
Jay = User()
Jay.setPassword = '12345678'
Jat.password

print(Jay.password_hash)

print(Jay.verify_password('12345678'))
print(Jay.verify_password(''))





 
    
    
    
    
    
    
    
    
    
    
    
    