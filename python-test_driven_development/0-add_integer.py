#!/usr/bin/python3
"""
Bu modul 'add_integer' funksiyasını ehtiva edir.
Bu modul Holberton/ALX layihəsi üçün hazırlanıb.
"""


def add_integer(a, b=98):
    """
    İki ədədi (int və ya float) toplayır və tam ədəd qaytarır.

    Arqumentlər:
        a: Birinci ədəd.
        b: İkinci ədəd (susmaya görə 98).

    Nəticə:
        İki ədədin cəmi (int).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
