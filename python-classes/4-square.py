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
        """
        self.size = size

    @property
    def size(self):
        """
        __size dəyərini geri qaytarır (Getter).

        Nəticə:
            Kvadratın ölçüsü.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        __size dəyərini təyin edir (Setter).

        Arqumentlər:
            value (int): Yeni ölçü dəyəri.

        Xətalar:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Kvadratın sahəsini hesablayır.

        Nəticə:
            Kvadratın sahəsi (int).
        """
        return self.__size ** 2
