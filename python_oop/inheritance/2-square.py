#!/usr/bin/env python3
"""Módulo que define una clase Square con su propia representación."""
BaseSquare = __import__('1-square').Square


class Square(BaseSquare):
    """Representa un cuadrado."""

    def __init__(self, size):
        """Inicializa un cuadrado con el tamaño dado."""
        super().__init__(size)
        self.__size = size

    def __str__(self):
        """Devuelve la descripción del cuadrado."""
        return f"[Square] {self.__size}/{self.__size}"
