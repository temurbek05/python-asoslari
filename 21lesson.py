# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 17:34:51 2024

@author: yuldo
"""

'''
1st problem def katta_harf(matn):
    for text in range(len(matn)):
        matn[text]= matn[text].capitalize()
    print(matn)
sentences_list = [
    "this is the first sentence.",
    "python is a powerful programming language.",
    "lists in Python can hold various types of elements.",
    "each element in the list is separated by a comma.",
    "let's create a list of sentences."
]
katta_harf(sentences_list[:])
print(sentences_list)
'''
def bahola(ismlar):
    baholar = {}
    for talaba in ismlar:
        baho = input(f"Talaba {talaba.title()}ning bahosini kiriting: ")
        baholar[talaba]=baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)