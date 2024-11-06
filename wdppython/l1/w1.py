######################################
#  hello.py
######################################

print (10 * 'Witamy na WdP!\n', end='\n\nNiech żyją nowe wiersze!\n\n')

for i in range(10):
    print ('Będzie dobrze!', end=' ')
    print (i)

######################################
#  kostki.py
######################################

import random

def kostka():
    return random.randint(1, 6)

licznik = 0
    
while True:
    a = kostka()
    b = kostka()
    licznik += 1
    print (a, b)
    if a == 6 and b == 6:
        break
        
print ('Licznik=', licznik)        
    

######################################
#  p1.py
######################################

from math import sqrt

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))

# print (a, b, c, a+b+c)

delta = b**2 - 4*a*c

if delta < 0:
    print ('Nie ma pierwiastków rzeczywistych')
    
if delta == 0:
    print ('x1 = x2 =', -b / (2*a) )
    
if delta > 0:
    print ('x1 =', (-b - sqrt(delta)) / (2*a))
    print ('x2 =', (-b + sqrt(delta)) / (2*a))
        
    print ('Pierwiastek z delta=', delta ** 0.5)
    print ('Pierwiastek z delta=', sqrt(delta))




######################################
#  p2.py
######################################

from math import sqrt

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))

# print (a, b, c, a+b+c)

delta = b**2 - 4*a*c

if delta < 0:
    print ('Nie ma pierwiastków rzeczywistych')
else:       
    if delta == 0:
        print ('x1 = x2 =', -b / (2*a) )        
    else:  # delta > 0:
        print ('x1 =', (-b - sqrt(delta)) / (2*a))
        print ('x2 =', (-b + sqrt(delta)) / (2*a))




######################################
#  p3.py
######################################

from math import sqrt

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))

# print (a, b, c, a+b+c)

delta = b**2 - 4*a*c

if delta < 0:
    print ('Nie ma pierwiastków rzeczywistych')    
elif delta == 0:
    print ('x1 = x2 =', -b / (2*a) )
else:
    print ('x1 =', (-b - sqrt(delta)) / (2*a))
    print ('x2 =', (-b + sqrt(delta)) / (2*a))
        





######################################
#  pierwsza_sesja.py
######################################

# coding: utf-8
2 * (3+4)
2 * (3+4) * 3
2 * (3+4) * 3 - 42
2 * 3 + 4
2 + 3 * 4
2 ** 10
2 ** 100
2 ** 1000
2 ** 10000
x = 2 ** 100000
1/2
(1/2) * 2
12.8495794859485
12.849579485948598674684768476
222222 / 2
222222 // 2
1234567 % 1000
1234567 // 1000
int(34 / 3)
float(int(34 / 3))
2 + 2 == 4
2 + 2 == 4.0
1 < 2
1 < 2 < 3
1 < 2 < 3 == 3 <= 10 == 5+5
1 < 2 < 3 == 3 <= 1 == 5+5
3 >= 3
10 != 10.0
1 < 2 and 2+2 == 4
1 > 2 and 0/0 == 14
1 < 2 and 0/0 == 14
1 < 2 or 0/0 == 14
not (2  == 2)
'to jest napis'
x = "La la la"
y = 'I powiedział: "Dość!"'
z = "My name's Bond. James Bond."
'kotek' == "kotek"
x + x
x + ' ' + x
3 * z
3 * (z + ' ')

######################################
#  potega.py
######################################

def potega(a, n):
    wynik = 1
    for i in range(n):
        wynik *= a  # rownoważne: wynik = wynik * a  
    return wynik
    
for i in range(1, 11):
    print (f'2 ** {i} == {potega(2,i)}')    

