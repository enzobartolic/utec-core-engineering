#!/usr/bin/env python3
"""Modulo que define una clase cuadrado con una validacion del tamaño"""

class Square:
    """Representa a un cuadrado"""

    def __init__(self, size=0):
        """Inicialisar a un cuadredo con la validacion de tamaño privado"""
        if not isintance(size, int):
            raise TypeError(size, int):
        if size < 0:
            raise ValueError("size muste be >= 0")
        self.__size = size