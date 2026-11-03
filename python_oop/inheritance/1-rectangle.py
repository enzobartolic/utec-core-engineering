#!/usr/bin/env python3
"""Módulo que define una clase Rectangle que hereda de BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo."""

    def __init__(self, width, height):
        """Inicializa un rectángulo validando ancho y alto."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
