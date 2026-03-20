#!/usr/bin/python3
"""
Bu modul 'matrix_divided' funksiyasını ehtiva edir.
Bu funksiya matrisin bütün elementlərini verilmiş rəqəmə bölür.
"""


def matrix_divided(matrix, div):
    """
    Matrisin bütün elementlərini div-ə bölür və 2 onluq işarəyə qədər yuvarlaqlaşdırır.

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

    # Matrisin list of lists olduğunu və boş olmadığını yoxla
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # Hər sətrin ölçüsünün eyni olduğunu yoxla
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # div-in rəqəm olduğunu yoxla
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 0-a bölməni yoxla
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Yeni matris yaradaraq bölmə əməliyyatını icra et
    return [[round(element / div, 2) for element in row] for row in matrix]
