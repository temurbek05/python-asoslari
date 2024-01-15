# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:55:13 2024

@author: yuldo
"""

savol = "Sevgan kitobingizni kiriting"
savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

while True:
    kitob = input(savol)
    if kitob == 'exit':
        break
print('Rahmat!')