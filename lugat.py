termin = {'integer':'butun',
          'float':'o`nli son',
          'boolean':'true, false',
          'if-else':'shartli operator'
    }
user_input = input("Biror so'z kiriting: ")
no_termin = termin.get(user_input, 'Bunday so`z mavjud emas')
print(no_termin)
