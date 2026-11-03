#!/usr/bin/env python3
"""Módulo que define una clase Square con posición y representación."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado con tamaño y posición validados."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece el tamaño del cuadrado validando tipo y valor."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Obtiene la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece la posición validando que sea una tupla de 2 enteros."""
        msg = "position must be a tuple of 2 positive integer"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(msg)
        if not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError(msg)
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con el carácter #."""
        print(self)

    def __str__(self):
        """Devuelve el cuadrado como texto, respetando la posición."""
        if self.__size == 0:
            return ""
        fila = " " * self.__position[0] + "#" * self.__size
        return "\n" * self.__position[1] + "\n".join(
            [fila] * self.__size)
