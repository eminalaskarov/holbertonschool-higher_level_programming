#!/usr/bin/python3
"""
Bu modul 'matrix_divided' funksiyasını ehtiva edir.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div-ə bölür.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # Matrisin tipini və boş olub-olmadığını yoxla
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    # Sətir ölçülərini yoxla
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # div-in rəqəm olub-olmadığını yoxla
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Sıfıra bölməni yoxla
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Bölmə və yuvarlaqlaşdırma
    # Qeyd: Əgər div sonsuzluq olsa, nəticə avtomatik 0.0 olacaq.
    return [[round(x / div, 2) for x in row] for row in matrix]
