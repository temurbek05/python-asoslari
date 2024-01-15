# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:19:07 2024

@author: yuldo
"""

countries = {
    'USA': {
        'capital': 'Washington, D.C.',
        'population': 331002651,
        'official_language': 'English',
        'currency': 'United States Dollar (USD)'
    },
    'India': {
        'capital': 'New Delhi',
        'population': 1380004385,
        'official_language': 'Hindi, English',
        'currency': 'Indian Rupee (INR)'
    },
    'China': {
        'capital': 'Beijing',
        'population': 1444216107,
        'official_language': 'Mandarin',
        'currency': 'Renminbi (CNY)'
    },
    'Brazil': {
        'capital': 'Brasília',
        'population': 212559417,
        'official_language': 'Portuguese',
        'currency': 'Brazilian Real (BRL)'
    }
}
country = input("Enter any country: ")
if country in countries:
  print(f"The capital of {country} is {countries[country]['capital']}, {countries[country]['population']} people live in it,  ",
        f"they speak {countries[country]['official_language']}")
else: print("We don't have information about this country")