#!/usr/bin/env python3
"""Módulo que define una clase base para figuras geométricas."""


class BaseGeometry:
    """Clase base con comportamiento compartido por las figuras."""

    def area(self):
        """Calcula el área; las subclases deben implementarlo."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que value sea un entero mayor que 0."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
