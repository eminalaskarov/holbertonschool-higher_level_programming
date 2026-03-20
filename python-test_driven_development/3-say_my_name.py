#!/usr/bin/python3
"""
Bu modul 'say_my_name' funksiyasını ehtiva edir.
Funksiya adı və soyadı çap etmək üçün nəzərdə tutulub.
"""


def say_my_name(first_name, last_name=""):
    """
    'My name is <first name> <last_name>' mətnini çap edir.

    Arqumentlər:
        first_name: Ad (string).
        last_name: Soyad (string), susmaya görə boşdur.

    Xətalar:
        TypeError: Əgər first_name və ya last_name string deyilsə.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
