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

    def __init__(self, size):
        """
        Yeni bir Square obyekti yaradır.

        Arqumentlər:
            size: Kvadratın ölçüsü.
        """
        self.__size = size
