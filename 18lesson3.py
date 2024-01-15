# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:48:01 2024

@author: yuldo
"""
products1 = {'jeans', 'boots', 'book', 'tv'}
ebook_products = {'tv': '300$', 'boots': '23$', 'hokkey ball': '15$', 'laptop': '900$'}
products = {}
'''
n = 1
while True :
    n = n+1
    product_name = input("Enter the name of the product: ")
    product_price = input(f"Enter the price of {product_name}: ")
    products[product_name]= product_price
    if n==5:
        break
print(products)
'''
for product in products1:
   if product in ebook_products:
       print(f"The price of {product} is {ebook_products[product]}")
      
''' 
      while products1:
    buyurtma = products1.pop()
    if buyurtma in ebook_products.keys():
        narh = ebook_products[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")'''