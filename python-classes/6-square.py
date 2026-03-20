#!/usr/bin/python3
"""
Bu modul 'Square' (Kvadrat) sinfini ehtiva edir.
"""


class Square:
    """
    Kvadratı təmsil edən sinif.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Yeni bir Square obyekti yaradır.

        Arqumentlər:
            size (int): Kvadratın ölçüsü.
            position (tuple): Kvadratın koordinatları (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """__size dəyərini geri qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """__size dəyərini yoxlayır və təyin edir."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """__position dəyərini geri qaytarır."""
        return self.__position

    @size.setter
    @position.setter
    def position(self, value):
        """
        __position dəyərini yoxlayır və təyin edir.
        Value mütləq 2 müsbət tam ədəddən ibarət tuple olmalıdır.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """
        Kvadratı '#' və 'position' nəzərə alınmaqla çap edir.
        """
        if self.__size == 0:
            print("")
            return

        # Yuxarıdan buraxılan boş sətirlər (position[1])
        for i in range(self.__position[1]):
            print("")

        # Kvadratın sətirləri
        for i in range(self.__size):
            # Soldan buraxılan boşluqlar (position[0])
            print(" " * self.__position[0] + "#" * self.__size)
