#!/usr/bin/env python3
"""Modulo que define a una clase cuadrado con tamaño privado"""


class Square:
    """Representa un cuadrado"""

    def __init__(self, size):
        """Inicialisar un cuadrdo privado."""
        self.__size = size
        