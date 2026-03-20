#!/usr/bin/python3
"""
Bu modul 'Rectangle' (Düzbucaqlı) sinfini ehtiva edir.
'BaseGeometry' sinfindən miras alır.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    BaseGeometry-dən miras alan Düzbucaqlı sinfi.
    """

    def __init__(self, width, height):
        """
        Yeni bir Rectangle obyekti yaradır.

        Arqumentlər:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
