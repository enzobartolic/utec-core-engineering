#!/usr/bin/env python3 
def uppercase(str):
    resultado = "" 
    for letra in str: 
        if ord(c) <= ord("z") and ord(c) >= ord("a"):
            nueva_letra = chr(ord(letra)+(ord("A")-ord("a")))
        else:
            nueva_letra = letra
        resultado = resultado + nueva_letra
    print(resultado)        