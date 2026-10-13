#!/usr/bin/env python3
def uppercase(str):
    resultado = ""
    for letra in str:
        if ord(letra) >= ord("a") and ord(letra) <= ord("z"):
            nueva_letra = chr(ord(letra) + (ord("A") - ord("a")))
        else:
            nueva_letra = letra
        resultado = resultado + nueva_letra
    print("{}".format(resultado))