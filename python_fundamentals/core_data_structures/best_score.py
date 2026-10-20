#!/usr/bin/env python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    mejor_clave = None
    mejor_valor = None
    for clave in a_dictionary:
        if mejor_valor is None or a_dictionary[clave] > mejor_valor:
            mejor_valor = a_dictionary[clave]
            mejor_clave = clave
    return mejor_clave
