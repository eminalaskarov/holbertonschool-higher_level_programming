#!/usr/bin/python3
"""
Bu modul 'matrix_divided' funksiyasını ehtiva edir.
Bu funksiya matrisin bütün elementlərini verilmiş rəqəmə bölür.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div-ə bölür.

    Arqumentlər:
        matrix: Siyahıların siyahısı (int və ya float).
        div: Bölən rəqəm (int və ya float).

    Xətalar:
        TypeError: Matris düzgün formatda deyilsə.
        TypeError: Sətirlərin ölçüsü eyni deyilsə.
        TypeError: div rəqəm deyilsə.
        ZeroDivisionError: div 0-a bərabərdirsə.

    Nəticə:
        Bölünmüş elementlərdən ibarət yeni matris.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
