#!/usr/bin/env python3
letras = ""
for numero in range(97, 123):
    letra = chr(numero)
    if letra != "e" and letra != "q":
        letras += letra
print("{}".format(letras))
