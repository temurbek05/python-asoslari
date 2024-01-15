# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:38:42 2024

@author: yuldo
"""
'''
1.   def yosh_hisobla():
    ism= input("Ismingiz nima? ")
    tugilgan_yil = int(input("Nechanchi yil tugilgansiz? "))
    yosh = 2024 - tugilgan_yil
    print(f"{ism}, siz {yosh} yoshdasiz")
yosh_hisobla()
'''
'''
2.   def kvadrat_hisobla():
    son = int(input("Istalgan son kiriting: "))
    kvadrat = son**2
    kub = son**3
    print(f"{son}ning kvadrati {kvadrat}, kubi esa {kub}")
kvadrat_hisobla()
'''
def bolinish_tekshiruvchi(son):
    for n in range(2,11):
        if son%n == 0:
            print(f"{son} {n} ga bo'linadi")
bolinish_tekshiruvchi(75)
        
        