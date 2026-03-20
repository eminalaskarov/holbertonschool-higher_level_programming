#!/usr/bin/python3
"""
Bu modul 'add_integer' funksiyasını ehtiva edir.
"""


def add_integer(a, b=98):
    """
    İki ədədi toplayır. a və b mütləq int və ya float olmalıdır.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # Əgər ədəd infinity (sonsuzluq) və ya NaN-dırsa, casting xəta verə bilər
    # Amma tapşırıq bizdən float-u int-ə çevirməyi tələb edir.
    
    return int(a) + int(b)
