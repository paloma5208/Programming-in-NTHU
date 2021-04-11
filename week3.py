# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:04:06 2020

@author: Paloma
"""

#物件導向3
#[變數]
x = 11 #global variable
def f():
    print('x in f():', x)
def g():
    x = 22 #當不是用g()這個函數，就不會把x = 22 call 出來
    print('x in g()')
            #class裡面的函數裡的x在呼叫class時也不會備call
            
"""
運算子多載：定義說當我看到某個符號，應該要做甚麼樣的運算
"""

class Number:
    def __init__(self, start):
        self.data = start
    
x = Number(5)
y = x - 2   #現在的算式不知道遇到減號要做甚麼
print(y)

#前面沒加sub時，不用用x - 2這個動作
#看到減號時，會把後面的value讀進來
#之前都是對數字加減乘除
#但其實在不同類別，都可以定義自己的加減乘除
#運算子多載：改變運算子，讓他可以去做你希望他做的動作

class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):   #當發現減號這個東西，就會自動把後面的value讀進來
        return self.data - other
        
    
x = Number(5)
y = x - 2
print(y)
            
#在int裡面有定義了很多運算子
#在這個類別裡面，python已經幫你定義好能做哪些運算

"""
exercise1
"""

#完成以下程式碼, 輸入 x, y 為 n x n 的矩陣, 當執行 x + y時, 請將 x,y 各項分別相加

class Matrix:
    def __init__(self, input_m):
        self.m = input_m
    def __add__(self, other):
        n = len(self.m)
        
        #先創造出一個n*n，元素全為0的矩陣
        #之後再更改該矩陣的元素
        #self是原本的input，other是後天輸進去的矩陣
        ans = [[0 for col in range(n)] for row in range(n)] 
        
        
        for i in range(0, n):
            for j in range(0, n):
                
                #other因為是定義好的矩陣所以也要.m
                ans[i][j] = self.m[i][j] + other.m[i][j]
        return ans
    
#矩陣相加就是把每個項目相加
x = Matrix([1,2],[3,4])
y = Matrix([3,4],[5,6])

answer = x + y
print(answer)
    

"""
exercise2
請完成一份程式碼
可以使用 < 比較a[i]是否小於b[i]，比較後的結果
"""
#每個 type 都是一個 class
#所以class可以繼承預設的變數類型
#重點是我們可以接收已知類別
#我們可以按照自己的邏輯重新定義符號要怎麼運算

class MyList(list):
    def __init__(self, value = []):
        list.__init__([])
        self.extend(value)
        
    def __lt__(self, other):
        ans = []
        for i in range(len(self)):
            if self[i] < other[i]:
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
            
"""
Generator
yield(迭代)可依序回傳(一直傳下一個給你)
return直接回傳結果
"""      
def nextSquare():
    i = 1
    while True:
        yield i * i
        i += 1
        
for i in nextSquare():
    if i > 100:
        break
    print(i)
"""
在定義class時可用__getitem__達到類似的效果
"""          

class Animal:
    def __init__(self, animal_list):
        self.animal_name = animal_list
        
animals = Animal(['dog', 'cat', 'fish'])
for animal in animals:
    print(animal)
    
class Animal:
    def __init__(self, animal_list):
        self.animal_name = animal_list
        
    def __getitem__(self, index):
        print(index)
        return self.animal_name[index]
    
for animal in animals:
    print(animal)
    
animals = Animal(['dog'])

"""
__iter__
當把東西寫在for裡面，就會一直傳下一個給你
會執行next裡面規定的事情
(1,5)很像range的概念
在for裡面會一直執行next
在寫next時要有一個停止的標準
"""

#raise:
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIterration
        
        self.value += 1
        return self.value ** 2
    
X = Squares(1,5)
for item in x:
    print(item)
    
X = Squares(1,5)
I = iter(X)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))

"""
作業
"""

#3/16、3/20都要包含在裡面喔！
#第二個作業改上次的程式碼即可