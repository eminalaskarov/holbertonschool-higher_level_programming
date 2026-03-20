#!/usr/bin/python3
"""
Bu modul 'add_integer' funksiyasını ehtiva edir.
Modulun məqsədi iki ədədi təhlükəsiz şəkildə toplamaqdır.
"""


def add_integer(a, b=98):
    """
    İki tam və ya onluq ədədi toplayır.

    Arqumentlər:
        a: Birinci ədəd (int və ya float).
        b: İkinci ədəd (int və ya float), susmaya görə 98.

    Xətalar:
        TypeError: Əgər a və ya b int/float deyilsə.

    Nəticə:
        İki ədədin cəmi (int).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
