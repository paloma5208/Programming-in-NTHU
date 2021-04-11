# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:45:09 2020

@author: Paloma
"""
import re

string = 'apple bird cat'
pattern1 = 'cat'
pattern2 = 'dog'
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)

print(result1)
print(result2)

"""
"""
#[] = 這個位置有多種可能
string1 = 'a run to b'
string2 = 'a ran to b'

pattern = r'r[ua]n'

result1 = re.search(pattern, string1)
result2 = re.search(pattern, string2)

print(result1)
print(result2)

"""
"""
string1 = 'a run to b'
string2 = 'a rUn to b'

pattern = r'r[A-Z]n'

result1 = re.search(pattern, string1)
result2 = re.search(pattern, string2)

print(result1)
print(result2)

"""
"""

string1 = 'a run to b'
string2 = 'a rUn to b'
string3 = 'a r3n to b'

pattern = r'r[A-Za-z]n'

result1 = re.search(pattern, string1)
result2 = re.search(pattern, string2)
result3 = re.search(pattern, string3)

print(result1)
print(result2)
print(result3)

"""
"""

string = 'run r3n'


pattern1 = r'r\dn' #數字
pattern2 = r'r\Dn' #數字以外

result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)


print(result1)
print(result2)

"""
"""
string = 'run r3n'


pattern1 = r'r\dn' #數字
pattern2 = r'r\Dn' #數字以外

result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)


print(result1)
print(result2)

"""
"""

string1 = 'a run to b'

pattern1 = r'^a'
pattern2 = r'b$'
pattern3 = r'r.n'

result1 = re.search(pattern1, string1)
result2 = re.search(pattern2, string1)
result3 = re.search(pattern3, string1)

print(result1)
print(result2)
print(result3)

"""
"""

string = '''
A run to B.
I run to A.
'''

print(re.search(r'^I', string))
print(re.search(r'^I', string, flags = re.M)) #flags讓python知道文章是多行的

"""
"""

#0或多次
print(re.search(r'ab*', 'abbbbb'))
print(re.search(r'ab*', 'a'))

#1或多次
print(re.search(r'ab+', 'a'))
print(re.search(r'ab+', 'abbbbb'))



"""
"""

#括號裡面的東西有會印出來，但沒有也沒關係
print(re.search(r'NTHU(QF)?', 'NTHU'))
print(re.search(r'NTHU(QF)?', 'NTHUQF'))
print(re.search(r'NTHU(QF)?', 'NTHUECO'))

"""
"""

result = re.search(r'(?P<id>\d+), Date: (?P<date>.+)', 'ID: 123456, Date: 2020/4/21')

print(result.group())
print(result.group('id'))
print(result.group('date'))

"""
"""
# +: 一或多次  #
result = re.search(r'(\d+), Date: (.+)', 'ID: 123456, Date: 2020/4/21')

print(result.group())
print(result.group(1))
print(result.group(2))

type(result)
"""
"""

compiled_re = re.compile(r'(\d+), Date: (.+)')
type
result = compiled_re.search('ID: 123456, Date: 2020/4/21') #從1開始計算
print(result)

"""
驗證身分證
"""
import re
if re.match(r'[A-Z][0-9]{9}$', input('請輸入身份證字號')): #match: 從頭開始找 #search: 可以從中間開始找
    print('正確')
else:
    print('錯誤')

"""
"""

from func import *
import datetime

now = datetime.datetime.now()

y = now.year - 1911
m - now.month - 1