# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:04:07 2024

@author: yuldo
"""
'''
3rd problem def findmax(x, y, z):
    if x > y and x > z:
        return x
    elif y>x and y>z:
        return y
    else: return z
#max_number = findmax(x, y, z)
a = findmax(1, 5, 3)
print(a)
'''
def find_prime(x, y):
    tub_sonlar = []
    for a in range(x,y):
        tub = True
        if a == 1:
            tub = False
        elif a==2:
            tub = True
        else:
            for b in range(2,a):
                if a%b==0:
                    tub = False
        if tub:
            tub_sonlar.append(a)
    print(tub_sonlar)
find_prime(3, 78)



                