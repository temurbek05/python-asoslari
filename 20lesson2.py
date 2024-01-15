# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:34:09 2024

@author: yuldo
"""
'''
def user_info(ismi, familiyasi, tugilgan_yili, tugilgan_joyi, email_manzili='', telefon_raqami=None):
    user_infos = {'ism': ismi,
                  'familiya': familiyasi,
                  'tugilgan_yil': tugilgan_yili,
                  'yoshi': 2024 - tugilgan_yili,
                  'tugilgan_joy': tugilgan_joyi,
                  'email_manzili': email_manzili,
                  'telefon_raqam': telefon_raqami
                  }
    return user_infos

print("Mijozlar haqida ma'lumotni kiriting")
mijozlar = []

while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tugilgan_yili = int(input("Tug'ilgan yili: "))
    tugilgan_joyi = input("Tug'ilgan joyi: ")
    email_manzili = input("Email: ")
    telefon_raqami = input("Telefon raqami: ")
    
    mijozlar.append(user_info(ism, familiya, tugilgan_yili, tugilgan_joyi, email_manzili, telefon_raqami))
    
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob.lower() != "ha":
        break

for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}, "
          f"{mijoz['yoshi']}-yoshda, "
          f"telefon raqami: {mijoz['telefon_raqam']}, "
          f"email: {mijoz['email_manzili']}")
'''