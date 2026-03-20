#!/usr/bin/python3
"""
Bu modul 'Square' (Kvadrat) sinfini ehtiva edir.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.

    Atributlar:
        __size (int): Kvadratın tərəfinin ölçüsü (private).
    """

    def __init__(self, size=0):
        """
        Yeni bir Square obyekti yaradır.

        Arqumentlər:
            size (int): Kvadratın ölçüsü, susmaya görə 0.

        Xətalar:
            TypeError: Əgər size integer deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
