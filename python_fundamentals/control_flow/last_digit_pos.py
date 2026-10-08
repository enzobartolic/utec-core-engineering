#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)
ultimo_digito = abs(number) % 10
if number < 0:
    ultimo_digito = -ultimo_digito
if ultimo_digito > 5:
    print("Last digit of", number, "is", ultimo_digito,
          "and is greater than 5")
elif ultimo_digito == 0:
    print("Last digit of", number, "is", ultimo_digito, "and is 0")
else:
    print("Last digit of", number, "is", ultimo_digito,
          "and is less than 6 and not 0")
